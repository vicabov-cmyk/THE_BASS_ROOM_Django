from django.test import TestCase
from django.urls import reverse


class NavigationTests(TestCase):
    def test_all_navigation_pages_open(self):
        for name in ('home', 'events', 'artists', 'about', 'contacts'):
            response = self.client.get(reverse('bassroom:' + name))
            self.assertEqual(response.status_code, 200, name)
            self.assertContains(response, 'THE BASS ROOM')

    def test_home_has_working_internal_links(self):
        response = self.client.get(reverse('bassroom:home'))
        for name in ('events', 'artists', 'about', 'contacts'):
            self.assertContains(response, reverse('bassroom:' + name))
