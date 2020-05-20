from django.test import TestCase


class PurBeurreTestViews(TestCase):

    def test_views_pur_beurre_home(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)

    def test_views_pur_beurre_legal_notice(self):
        response = self.client.get("/legal_notice/")
        self.assertEqual(response.status_code, 200)
