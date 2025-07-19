from django.conf import settings
from django.db import models

user = settings.AUTH_USER_MODEL


class Document(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        to=user, on_delete=models.CASCADE, related_name="authored_documents"
    )
    reviewers = models.ManyToManyField(
        to=user, related_name="reviewed_documents"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"
        ordering = ["-created_at"]
