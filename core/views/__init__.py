from django.http import HttpResponse
from django.shortcuts import render
from .create import CreateView

def index(request) -> HttpResponse:
    return render(request=request, template_name="core/index.html")


