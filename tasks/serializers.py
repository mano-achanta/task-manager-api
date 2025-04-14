from rest_framework import serializers
from .models import Task, CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'mobile']


class TaskSerializer(serializers.ModelSerializer):
    assigned_users = UserSerializer(many=True, read_only=True)
    assigned_user_ids = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(), many=True, write_only=True, source='assigned_users'
    )

    class Meta:
        model = Task
        fields = [
            'id', 'name', 'description', 'created_at', 'task_type',
            'completed_at', 'status', 'assigned_users', 'assigned_user_ids'
        ]

    def validate(self, data):
        if not data.get('name'):
            raise serializers.ValidationError({"name": "Task name is required."})
        return data