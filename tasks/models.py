from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Administrator'),
        ('user', 'Standard User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.username} ({self.role})"

    def is_admin(self):
        return self.role == 'admin'


class Project(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project_list')


class Task(models.Model):
    PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )

    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, related_name='tasks')
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_tasks')
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='assigned_tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title