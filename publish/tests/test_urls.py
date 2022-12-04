from django.test import SimpleTestCase
from django.urls import reverse, resolve
from publish.views import publish_index, create_ride


class TestUrl(SimpleTestCase):

    def test_publish_index_resolved(self):
        url = reverse('publish')
        self.assertEquals(resolve(url).func, publish_index)

    def test_create_ride_resolved(self):
        url = reverse('create_ride')
        self.assertEquals(resolve(url).func, create_ride)
