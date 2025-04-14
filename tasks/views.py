from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task, CustomUser
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        """Create a new task."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'], url_path='assign')
    def assign_task(self, request, pk=None):
        """Assign the task to one or more users."""
        task = self.get_object()
        user_ids = request.data.get('user_ids', [])
        if not user_ids:
            return Response(
                {"error": "At least one user ID is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            users = CustomUser.objects.filter(id__in=user_ids)
            task.assigned_users.set(users)
            serializer = self.get_serializer(task)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response(
                {"error": "One or more user IDs are invalid."},
                status=status.HTTP_400_BAD_REQUEST
            )

    @action(detail=False, methods=['get'], url_path='user/(?P<user_id>\d+)')
    def get_user_tasks(self, request, user_id=None):
        """Retrieve all tasks assigned to a specific user."""
        try:
            user = CustomUser.objects.get(id=user_id)
            tasks = Task.objects.filter(assigned_users=user)
            serializer = self.get_serializer(tasks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response(
                {"error": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )