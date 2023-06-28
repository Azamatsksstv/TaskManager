from rest_framework import generics
from tasks.models import Task
from tasks.serializers import TaskSerializer


class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CreateTask(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class DetailTask(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        task_id = self.kwargs['pk']
        queryset = Task.objects.filter(id=task_id)
        return queryset


class UpdateTask(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class DeleteTask(generics.RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

