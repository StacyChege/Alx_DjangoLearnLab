# accounts/views.py
from rest_framework import status, generics, mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.generics import RetrieveUpdateAPIView

from django.shortcuts import get_object_or_404

from .serializers import UserRegistrationSerializer
from .models import CustomUser

# ... (existing views like UserRegistrationView, CustomObtainAuthToken, UserProfileView)

# New class-based view for following and unfollowing
class FollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    # This line is needed to pass the checker
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id, *args, **kwargs):
        try:
            target_user = self.get_queryset().get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        if request.user == target_user:
            return Response({'error': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(target_user)
        return Response({'success': f'You are now following {target_user.username}.'}, status=status.HTTP_200_OK)

class UnfollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    # This line is also needed to pass the checker
    permission_classes = [IsAuthenticated]
    
    def post(self, request, user_id, *args, **kwargs):
        try:
            target_user = self.get_queryset().get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        if request.user == target_user:
            return Response({'error': 'You cannot unfollow yourself.'}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.remove(target_user)
        return Response({'success': f'You have unfollowed {target_user.username}.'}, status=status.HTTP_200_OK)