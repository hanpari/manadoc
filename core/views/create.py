from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.forms import ModelForm
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
