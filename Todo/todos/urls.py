from django.urls import path
from . import views

urlpatterns = [
    path('create-todo', views.create_todo, name='create_todo'),
    path('list-todo', views.view_todo, name='list_todo'),
    path('update-todo/<int:pk>', views.update_todo, name='update_todo'),
    path('delete-todo/<int:pk>', views.delete_todo, name='delete_todo')
]