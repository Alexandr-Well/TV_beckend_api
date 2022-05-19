from rest_framework import viewsets, status
from .serializers import TaskSerializer
from .models import Task


class TaskViewSet(viewsets.ModelViewSet):
    """API для получения задачь пользователя"""
    serializer_class = TaskSerializer

    def get_queryset(self):
        if self.request.query_params.get('id') == 'null':
            return []  # Response({"Invalid": "Invalid user!!"}, status=status.HTTP_404_NOT_FOUND)
        if self.request.query_params.get('date'):
            return Task.objects.filter(date=self.request.query_params.get('date'),
                                       name=int(self.request.query_params.get('id')))
        return []  # Response({"Invalid": "error"}, status=status.HTTP_404_NOT_FOUND)
