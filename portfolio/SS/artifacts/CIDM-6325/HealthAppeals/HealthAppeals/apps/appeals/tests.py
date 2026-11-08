from django.test import TestCase
from django.urls import reverse

class BasicTests(TestCase):
    def test_generate_letter_page_loads(self):
        response = self.client.get(reverse("appeals:generate_letter"))
        self.assertEqual(response.status_code, 200)
