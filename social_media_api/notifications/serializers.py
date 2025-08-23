# notifications/serializers.py
from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.ReadOnlyField(source='actor.username')
    target = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ['id', 'actor', 'verb', 'target', 'timestamp', 'is_read']

    def get_target(self, obj):
        # A helper to return a string representation of the target object
        if obj.target:
            return str(obj.target)
        return None