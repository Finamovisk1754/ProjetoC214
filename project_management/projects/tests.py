from django.test import TestCase
from django.contrib.auth.models import User
from projects.models import Projeto, Tarefa , status
from rest_framework.test import APIClient

class ProjetoModelTests(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(username='teste_usuario', password='senha')  
        self.projeto = Projeto.objects.create(
            nome='Projeto de Teste',  
            descricao='Descrição do projeto',
            data_inicio='2024-01-01',
            data_fim='2024-12-31',
            responsavel=self.usuario
        )

    def test_projeto_criacao(self):
        self.assertEqual(self.projeto.nome, 'Projeto de Teste')  
        self.assertEqual(self.projeto.responsavel.username, 'teste_usuario')

class TarefaModelTests(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(username='teste_usuario', password='senha') 
        self.projeto = Projeto.objects.create(
            nome='Projeto de Teste',  
            descricao='Descrição do projeto',
            data_inicio='2024-01-01',
            data_fim='2024-12-31',
            responsavel=self.usuario
        )
        self.tarefa = Tarefa.objects.create(
            projeto=self.projeto,
            nome='Tarefa de Teste',  
            descricao='Descrição da tarefa',
            data_conclusao='2024-06-01', 
            concluida=False
        )

    def test_tarefa_criacao(self):
        self.assertEqual(self.tarefa.nome, 'Tarefa de Teste')  
        self.assertFalse(self.tarefa.concluida)

class TaskAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='teste_usuario', password='senha')
        self.client.login(username='teste_usuario', password='senha')
        self.project = Projeto.objects.create(
            name='Projeto de Teste',  
            descricao='Descrição do projeto', 
            data_inicio='2024-01-01',
            data_fim='2024-12-31',
            responsavel=self.user
        )
        self.tarefa = Tarefa.objects.create(  #
            projeto=self.project,
            nome='Tarefa de Teste',  
            descricao='Descrição da tarefa',  
            data_conclusao='2024-06-01',  
            concluida=False
        )

    def test_get_tasks(self):
        response = self.client.get('/api/tarefas/')  
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        data = {
            'projeto': self.project.id,
            'nome': 'Nova Tarefa',  
            'descricao': 'Descrição da nova tarefa',  
            'data_conclusao': '2024-06-01',  
            'concluida': False
        }
        response = self.client.post('/api/tarefas/', data) 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

