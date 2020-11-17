from django.test import TestCase
from emphasoft_app.models import Profile
from django.contrib.auth.models import User


class TestProfile(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="test", password="test")

    def test_user_instance_creation_crates_an_profile_instance(self):
        self.assertNotEqual(self.user.profile, None)

    def test_user_instance_saving_saves_an_profile_instance(self):
        self.user.profile.bio = 'test'
        with self.assertRaises(Profile.DoesNotExist):
            Profile.objects.get(bio='test')
        self.user.save()
        self.assertNotEqual(Profile.objects.get(bio='test'), None)
