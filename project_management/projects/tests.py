from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Project, Task


class ProjectTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.project = Project.objects.create(name='Test Project', description='Test Description', created_by=self.user)

    def test_create_task(self):
        url = reverse('create_task', args=[self.project.id])
        response = self.client.post(url, {
            'name': 'Task 1',
            'description': 'Task Description',
            'assignee': self.user.id,
            'due_date': '2024-06-30'
        })
        self.assertEqual(response.status_code, 302)  # Redirecionamento após criação

        # Verificar se a tarefa foi criada
        task_count = Task.objects.filter(name='Task 1').count()
        self.assertEqual(task_count, 1)


