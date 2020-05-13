from django.test import TestCase

from users.models import User

class UsersModelTest(TestCase):

    @classmethod
    def set_Up_Data(cls):
        User.objects.create_user(first_name="utilisateur", last_name="Test")
