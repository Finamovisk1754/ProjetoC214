# Sistema de gerenciamento de projetos
Este projeto é um sistema de gerenciamento de projetos desenvolvido com Django. Ele permite aos usuários criar, visualizar e gerenciar projetos e suas respectivas tarefas. Abaixo estão as principais funcionalidades do sistema:

## Funcionalidades Principais
1.	Autenticação de Usuários:  
	•	Registro de Usuários: Permite que novos usuários se registrem no sistema.  
	•	Login/Logout: Autenticação de usuários com opções de login e logout.  
2.	Gerenciamento de Projetos:  
	•	Criação de Projetos: Usuários podem criar novos projetos fornecendo um nome e uma descrição.  
	•	Visualização de Projetos: Lista de todos os projetos criados pelo usuário.  
	•	Detalhes do Projeto: Página detalhada que exibe informações sobre um projeto específico, incluindo nome, descrição, data de criação, data de atualização e proprietário.  
3.	Gerenciamento de Tarefas:  
	•	Criação de Tarefas: Adicionar tarefas a projetos existentes com nome, descrição, data de vencimento e responsável.  
	•	Visualização de Tarefas: Exibe todas as tarefas associadas a um projeto, incluindo detalhes como nome, descrição, data de vencimento, status de conclusão e responsável.  

## Configurações Iniciais
1.	Configuração do Ambiente Virtual:  
	•	Navegue até o diretório do projeto.  
	•	Ative o ambiente virtual que está na pasta .venv.  
```
  cd path/to/project_management/10
  source .venv/bin/activate
```
2.	Instalação das Dependências:
	•	Instale as dependências listadas no arquivo requirements.txt, se houver.
```
  pip install -r requirements.txt
```
3.  Configuração do Banco de Dados:
	•	Verifique se o banco de dados SQLite (db.sqlite3) está no diretório correto. Se estiver usando um banco de dados diferente, configure-o no arquivo settings.py.  
	•	Aplique as migrações para garantir que o banco de dados está atualizado.  
```
  python manage.py migrate
```

## Execução
1.	Criação de um Superusuário:
	•	Crie um superusuário para acessar a interface de administração do Django.
```
  python manage.py createsuperuser
```
2.	Execução do Servidor de Desenvolvimento:
	•	Inicie o servidor de desenvolvimento do Django.
```
  python manage.py runserver
```

## Acesso ao projeto
•	Abra um navegador e acesse http://127.0.0.1:8000.  
•	Faça login com o superusuário que você criou.  
•	Navegue até a URL http://127.0.0.1:8000/project/<project_id>/ para visualizar os detalhes de um projeto específico. Substitua <project_id> pelo ID de um projeto existente no banco de dados.  
