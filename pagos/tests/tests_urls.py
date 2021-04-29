from django.test import SimpleTestCase
from django.urls import reverse, resolve
from pagos.views import pagos_arriendos

class TestsUrls(SimpleTestCase):
    def test_url(self):
        url = reverse('pago')
        print(resolve(url))
        self.assertEquals(resolve(url).func, pagos_arriendos)