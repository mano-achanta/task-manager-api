from django.test import TestCase
from rest_framework.test import APIClient
from .models import Task, CustomUser


class TaskAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = CustomUser.objects.create_user(username='user1', password='pass123', email='user1@example.com', mobile='1234567890')
        self.user2 = CustomUser.objects.create_user(username='user2', password='pass123', email='user2@example.com', mobile='0987654321')
        self.task_data = {
            'name': 'Test Task',
            'description': 'Test Description',
            'task_type': 'GENERAL',
            'assigned_user_ids': [self.user1.id]
        }

    def test_create_task(self):
        response = self.client.post('/api/tasks/', self.task_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().name, 'Test Task')

    def test_assign_task(self):
        task = Task.objects.create(name='Test Task', description='Test', task_type='GENERAL')
        response = self.client.post(f'/api/tasks/{task.id}/assign/', {'user_ids': [self.user1.id, self.user2.id]}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(task.assigned_users.count(), 2)

    def test_get_user_tasks(self):
        task = Task.objects.create(name='Test Task', description='Test', task_type='GENERAL')
        task.assigned_users.add(self.user1)
        response = self.client.get(f'/api/tasks/user/{self.user1.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Test Task')