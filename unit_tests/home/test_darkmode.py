from django.test import TestCase, Client
from django.urls import reverse

class DarkModeTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.response = self.client.get(reverse('home'))

    def test_status_code(self):
        """La page d'accueil répond correctement"""
        self.assertEqual(self.response.status_code, 200)

    def test_contains_darkmode_toggle_button(self):
        """Le bouton de bascule Dark Mode est présent"""
        self.assertContains(self.response, 'id="darkModeToggle"')

    def test_contains_darkmode_script_function(self):
        """La fonction setDarkMode est présente dans le script JS"""
        self.assertContains(self.response, 'function setDarkMode(')

    def test_contains_darkmode_class_in_css(self):
        """La classe CSS .dark-mode est bien définie"""
        self.assertContains(self.response, 'body.dark-mode')
