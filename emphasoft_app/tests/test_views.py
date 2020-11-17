from django.test import TestCase, Client
from django.urls import reverse
from emphasoft_app.views import user_page
from django.contrib.auth.models import User


class TestUserPage(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test', password='test')
        self.user.save()
        self.client = Client()
        self.client.force_login(user=self.user)

    def test_is_available_by_id(self):
        response = self.client.get(reverse(
            'emphasoft_app:user', kwargs={'user_id': User.objects.get(username='test').id}
        ))
        self.assertEqual(response.status_code, 200)

    def test_response_is_404_if_user_does_not_exist(self):
        response = self.client.get(reverse(
            'emphasoft_app:user', kwargs={'user_id': 2}
        ))
        self.assertEqual(response.status_code, 404)
