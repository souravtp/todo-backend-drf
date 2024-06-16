from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import PermissionDenied

from .serializers import TodoSerializer
from .models import Todo
# Create your views here.


@api_view(['POST',])
def create_todo(request):
    data = request.data
    data['user'] = request.user.id
    todo = TodoSerializer(data=data)

    if todo.is_valid():
        todo.save()
        return Response(todo.data, status=status.HTTP_201_CREATED)

    else:
        return Response(todo.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def view_todo(request):
    todos = Todo.objects.filter(user=request.user)
    serializer = TodoSerializer(todos, many=True)

    return Response(serializer.data)


@api_view(['GET', 'PATCH'])
def update_todo(request, pk):
    todo = Todo.objects.get(id=pk)
    user = request.user

    if todo.user == user:
        if request.method == 'GET':
            serializer = TodoSerializer(todo)
            return Response(serializer.data)
        elif request.method == 'PATCH':
            serializer = TodoSerializer(instance=todo, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        raise PermissionDenied("you dont have permission to edit this.")


@api_view(['DELETE'])
def delete_todo(request, pk):
    todo = Todo.objects.get(id=pk)
    user = request.user

    if todo.user == user:
        todo.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    else:
        raise PermissionDenied('you have no permission to delete this view')
