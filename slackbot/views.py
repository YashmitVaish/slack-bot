from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .app import handler

@csrf_exempt
def slack_events(request):
    return handler.handle(request)

def healthz(request):
    return HttpResponse('ok')
