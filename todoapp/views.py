from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TodoItem
from .serializers import TodoItemSerializer

@api_view(['GET'])
def get_todos(request):
    todos = TodoItem.objects.all()
    serializer = TodoItemSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_todo(request):
    serializer = TodoItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_todo(request, pk):
    todo = TodoItem.objects.get(id=pk)
    todo.delete()
    return Response('Todo Deleted')
@api_view(['PUT'])
def update_todo(request, pk):
    todo = TodoItem.objects.get(id=pk)
    serializer = TodoItemSerializer(instance=todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

