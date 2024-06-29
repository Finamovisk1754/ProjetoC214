from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('', auth_views.LoginView.as_view(template_name='projects/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register_user, name='register'),
    path('home/', views.home_page, name='home'),
    path('create/', views.create_project, name='create_project'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('project/<int:project_id>/delete/', views.delete_project, name='delete_project'),
    path('project/<int:project_id>/create_task/', views.create_task, name='create_task'),
    path('task/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('task/<int:task_id>/upload_response/', views.upload_task_response, name='upload_task_response'),
    path('response/<int:response_id>/delete/', views.delete_task_response, name='delete_task_response'),
    path('response/<int:response_id>/view/', views.view_task_response, name='view_task_response'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
