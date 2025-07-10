from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from ..models import Document


class BasicCoreTests(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username="coreuser", password="testpassword", is_staff=True
        )

    def testIsOn(self):
        Document.objects.create(title="Title", content="Content", author=self.user)
