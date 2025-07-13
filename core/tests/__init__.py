from django.contrib.auth import get_user_model
from django.test import TestCase
from shared import FAKE_PASSWORD
from core.models import Document

User = get_user_model()


class BasicCoreTests(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(  # type: ignore
            username="coreuser",
            password=FAKE_PASSWORD,
            is_staff=True,
        )

    def testIsOn(self):
        Document.objects.create(
            title="Title", content="Content", author=self.user
        )
