from django.contrib import admin
from django.urls import path
from todoapp.views import todoappView
from todoapp.views import todoappView, addTodoView
from todoapp.views import todoappView, addTodoView, deleteTodoView 
from.import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todoapp/', views.todoappView),
    path('addTodoItems/',views.addTodoView),
    path('deleteTodoItems/<int:i>/',views.deleteTodoView), 

] 