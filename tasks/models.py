from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class CustomUser(AbstractUser):
    mobile = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username


class Task(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
    )

    TASK_TYPE_CHOICES = (
        ('GENERAL', 'General'),
        ('URGENT', 'Urgent'),
        ('LOW_PRIORITY', 'Low Priority'),
    )

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(max_length=20, choices=TASK_TYPE_CHOICES, default='GENERAL')
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    assigned_users = models.ManyToManyField(CustomUser, related_name='tasks')

    def __str__(self):
        return self.name

    def mark_completed(self):
        self.status = 'COMPLETED'
        self.completed_at = timezone.now()
        self.save()