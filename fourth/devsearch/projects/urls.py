from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.projects, name='projects'), # все проекты
    path('project/<str:pk>/', views.project, name='project'), # просмотр одного проекта

    path('create-project/', views.create_project, name='create-project'), # создание проекта
    path('update-project/<str:pk>/', views.update_project, name='update-project'),
    path('delete-project/<str:pk>/', views.delete_project, name='delete-project'),

]
