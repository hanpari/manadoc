from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class ManadocBasicTests(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username="testuser", password="testpassword", is_staff=True
        )

    def test_admin_page(self):
        response = self.client.get(reverse("admin:index"))
        self.assertEqual(
            response.status_code, 302
        )  # Redirect to login if not authenticated

    def test_admin_page_after_login(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("admin:index"))
        self.assertEqual(response.status_code, 200)

    def test_root_url_returns_200(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Controlled documentation")
