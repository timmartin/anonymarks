import os
import boto

from django.shortcuts import render
from django.core.context_processors import csrf

def home(request):
    context = {}
    return render(request, 'index.html', context)

def show(request):
    context = {}
    context.update(csrf(request))
    return render(request, 'show.html', context)
