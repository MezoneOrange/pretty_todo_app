from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add_todo, name='add'),
    path('complete/<int:todo_id>', views.complete_todo, name='complete'),
    path('delete-completed', views.delete_completed, name='delete-completed'),
    path('delete-all', views.delete_all, name='delete-all')
]