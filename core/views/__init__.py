from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.forms import ModelForm
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from ..models.document import Document


class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'content']


class DocumentCreateView(LoginRequiredMixin, CreateView):
    model = Document
    form_class = DocumentForm
    success_url = reverse_lazy("home")
    login_url = reverse_lazy("login")

    template_name = "core/create_document.html"

    def form_valid(self, form: DocumentForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)


class DocumentUpdateView(LoginRequiredMixin, UpdateView):
    model = Document
    form_class = DocumentForm
    success_url = reverse_lazy("home")
    login_url = reverse_lazy("login")
    template_name = "core/create_document.html"


class DocumentListView(ListView):
    model = Document
    template_name = "core/index.html"
    context_object_name = "documents"


class DocumentDetailView(LoginRequiredMixin, DetailView):
    pass


class DocumentDeleteView(UserPassesTestMixin, DeleteView):
    model = Document
    context_object_name = "document"
    template_name = "core/delete_document.html"
    success_url = reverse_lazy("home")

    def test_func(self) -> bool | None:
        document = self.get_object()
        return self.request.user == document.author

    def handle_no_permission(self) -> HttpResponseRedirect:
        messages.error(
            self.request, f"Login first to delete {self.get_object()} !"
        )
        return redirect("home")
