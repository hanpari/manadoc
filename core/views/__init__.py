from django.http import HttpResponse
from django.shortcuts import render
from .create import DocumentCreateView  # noqa: F401


def index(request) -> HttpResponse:
    return render(request=request, template_name="core/index.html")
