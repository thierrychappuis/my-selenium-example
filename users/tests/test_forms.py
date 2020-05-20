from django.test import TestCase

from users.forms import CustomUserCreationForm


class UsersFormTestCase(TestCase):

    def test_user_creation_forms_is_valid(self):
        form = CustomUserCreationForm(data={
            "username": "benjamin",
            "email": "benjamin@test.com",
            "first_name": "user",
            "last_name": "test",
            "password1": "Rita&122055",
            "password2": "Rita&122055"
            })
        self.assertTrue(form.is_valid())

    def test_user_creation_forms_is_not_valid(self):
        form = CustomUserCreationForm(data={
            "username": "benjamin",
            "email": "benjamin@test.com",
            "first_name": "user",
            "last_name": "test",
            "password1": "Rita&122055",
            "password2": "Azerty"
        })
        self.assertFalse(form.is_valid())

    def test_user_creation_forms_email_is_not_valid(self):
        form = CustomUserCreationForm(data={
            "username": "benjamin",
            "email": "benjamintest.com",
            "first_name": "user",
            "last_name": "test",
            "password1": "Rita&122055",
            "password2": "Rita&122055"
        })
        self.assertFalse(form.is_valid())
