from django.forms import ModelForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from ..models.document import Document


class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'content', "author"]


class DocumentCreateView(CreateView):
    model = Document
    form_class = DocumentForm
    success_url = reverse_lazy("home")
    template_name = "core/create_document.html"


class DocumentUpdateView(UpdateView):
    model = Document
    form_class = DocumentForm
    success_url = reverse_lazy("home")
    template_name = "core/create_document.html"


class DocumentListView(ListView):
    model = Document
    template_name = "core/index.html"
    context_object_name = "documents"
