from django.test import TestCase, Client
from django.urls import reverse

class DarkModeTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_homepage_contains_darkmode_toggle(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'id="darkModeToggle"')

    def test_homepage_contains_darkmode_script(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'function toggleDarkMode()')

    def test_homepage_contains_darkmode_class(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'dark-mode')