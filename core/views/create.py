from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView as DjangoCreateView

from ..models.document import Document


class CreateView(DjangoCreateView):
    model = Document
    fields = ["title", "content"]
    success_url = reverse_lazy("home")
    template_name = "core/create.html"

    def get(self, request, *args, **kwargs) -> HttpResponse:
        return render(request, self.template_name)  # type: ignore

    def post(self, request, *args, **kwargs) -> HttpResponse:

        return render(request, template_name=self.template_name)  # type: ignore
