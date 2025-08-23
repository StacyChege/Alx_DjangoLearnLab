# posts/views.py
from rest_framework import viewsets, mixins, generics, filters, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from notifications.models import Notification

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['author', 'title']
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.GenericViewSet, 
                     mixins.CreateModelMixin, 
                     mixins.RetrieveModelMixin, 
                     mixins.DestroyModelMixin, 
                     mixins.UpdateModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentListCreateView(viewsets.GenericViewSet, 
                            mixins.ListModelMixin, 
                            mixins.CreateModelMixin):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        post = Post.objects.get(id=post_id)
        serializer.save(author=self.request.user, post=post)

class UserFeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        
        # Check if user has already liked the post
        if Like.objects.filter(user=user, post=post).exists():
            return Response({'detail': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)
        
        Like.objects.create(user=user, post=post)
        
        # Create a notification for the post author
        if user != post.author:
            content_type = ContentType.objects.get_for_model(Post)
            Notification.objects.create(
                recipient=post.author,
                actor=user,
                verb='liked',
                content_type=content_type,
                object_id=post.id
            )

        return Response({'detail': 'Post liked successfully.'}, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def unlike(self, request, pk=None):
        post = self.get_object()
        user = request.user
        
        try:
            like = Like.objects.get(user=user, post=post)
            like.delete()
            return Response({'detail': 'Post unliked successfully.'}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({'detail': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)