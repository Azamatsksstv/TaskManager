from django.urls import path
from tasks.views import TaskList, CreateTask, DetailTask, UpdateTask, DeleteTask
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

urlpatterns = [
    path('', TaskList.as_view()),
    path('create/', CreateTask.as_view()),
    path('<int:pk>/', DetailTask.as_view()),
    path('<int:pk>/update/', UpdateTask.as_view()),
    path('<int:pk>/delete/', DeleteTask.as_view()),
]

urlpatterns += router.urls
