from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TaskSerializer
from .models import Task
# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str-pk>/',
        'Create': '/task-create/',
        'Delete': '/task-update/<str-pk>/',
        'Update': '/task-delete/<str-pk>/',
    }
    return Response(api_urls)

# list of responses so that we can see all of the data in our database
# we have couple of task so couple of item that will be rendered out from todo list
@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all().order_by('-id')
    # it serializes data specified and many=true means it serialize all query
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)
    # it will query our db serialize the data and return it in our api response


@api_view(['GET'])
def taskDetail(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    # in this we are getting the data as json object and the data we are passing is also a json form
    serializer = TaskSerializer(data=request.data)

    if(serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)
    # it will return data that get serialized


@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if(serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Item Successfully deleted")
