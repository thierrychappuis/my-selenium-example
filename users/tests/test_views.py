from django.test import TestCase

from users.models import User


class UsersTestViews(TestCase):

    def setUp(self):
        User.objects.create_user(
            username="UserTest", password="PaswordTest&120")

    def test_user_profile(self):
        self.client.login(username="UserTest", password="PaswordTest&120")
        response = self.client.get("/users/profile/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("users/profile.html")

    def test_user_create_account_successfully(self):
        response = self.client.post("/users/create_account/",
                                    {
                                        "username": "TestUser",
                                        "password1": "PasswordTest&120",
                                        "password2": "PasswordTest&120"
                                    })
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('users/profile.html')
