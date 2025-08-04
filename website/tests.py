from django.test import TestCase
from django.urls import reverse

class WebsiteViewTests(TestCase):
    def test_index_view_status_code(self):
        response = self.client.get(reverse('website:index'))
        self.assertEqual(response.status_code, 200)

    def test_a_propos_view_status_code(self):
        response = self.client.get(reverse('website:a-propos'))
        self.assertEqual(response.status_code, 200)

    def test_checkout_view_status_code(self):
        response = self.client.get(reverse('website:checkout'))
        self.assertEqual(response.status_code, 200)

    def test_communaute_view_status_code(self):
        response = self.client.get(reverse('website:communaute'))
        self.assertEqual(response.status_code, 200)

    def test_confirmation_view_status_code(self):
        response = self.client.get(reverse('website:confirmation'))
        self.assertEqual(response.status_code, 200)

    def test_consulting_view_status_code(self):
        response = self.client.get(reverse('website:consulting'))
        self.assertEqual(response.status_code, 200)

    def test_contact_view_status_code(self):
        response = self.client.get(reverse('website:contact'))
        self.assertEqual(response.status_code, 200)

    def test_coworking_view_status_code(self):
        response = self.client.get(reverse('website:coworking'))
        self.assertEqual(response.status_code, 200)

    def test_offres_view_status_code(self):
        response = self.client.get(reverse('website:offres'))
        self.assertEqual(response.status_code, 200)

    def test_suite_view_status_code(self):
        response = self.client.get(reverse('website:suite'))
        self.assertEqual(response.status_code, 200)
