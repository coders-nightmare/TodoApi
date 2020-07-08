from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def apiOverview(request):
    return JsonResponse("API BASE POINT", safe=False)
