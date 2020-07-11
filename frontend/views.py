from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.


def list(request):
    return render(request, 'frontend/list.html')
