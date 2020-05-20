from django.test import TestCase
from django.urls import resolve
from django.shortcuts import reverse

from pur_beurre.views import home, legal_notice


class UrlTestCase(TestCase):

    def test_home_url_view(self):
        found = resolve(reverse("home"))
        self.assertEqual(found.func, home)

    def test_legal_notice_url_view(self):
        found = resolve(reverse("legal_notice"))
        self.assertEqual(found.func, legal_notice)
