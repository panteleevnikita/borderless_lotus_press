from django.test import TestCase
from . import views


class TestsViews(TestCase):

    def test_index_view(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
