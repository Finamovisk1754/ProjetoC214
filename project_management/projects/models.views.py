from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from projects.models import Project, Task

class ProjectAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='teste_usuario', password='senha')
        self.client.login(username='teste_usuario', password='senha')
        self.project = Project.objects.create(
            name='Test Project',
            description='Project description',
            start_date='2024-01-01',
            end_date='2024-12-31',
            owner=self.user
        )

    def test_get_projects(self):
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_project(self):
        data = {
            'name': 'New Project',
            'description': 'New project description',
            'start_date': '2024-01-01',
            'end_date': '2024-12-31',
            'owner': self.user.id
        }
        response = self.client.post('/api/projects/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TaskAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='teste_usuario', password='senha')
        self.client.login(username='teste_usuario', password='senha')
        self.project = Project.objects.create(
            name='Test Project',
            description='Project description',
            start_date='2024-01-01',
            end_date='2024-12-31',
            owner=self.user
        )
        self.task = Task.objects.create(
            project=self.project,
            name='Test Task',
            description='Task description',
            due_date='2024-06-01',
            completed=False
        )

    def test_get_tasks(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        data = {
            'project': self.project.id,
            'name': 'New Task',
            'description': 'New task description',
            'due_date': '2024-06-01',
            'completed': False
        }
        response = self.client.post('/api/tasks/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
