from django.test import TestCase
from ..models import Pago


class PagoTest(TestCase):
    """ Test module for Pago model """

    def setUpTestData(self):
        Pago.objects.create(
            fechaPago='2021-04-29', documentoIdentificacionArrendatario=3, codigoInmueble="alpha1", valorPagado=200000)
        Pago.objects.create(
            fechaPago='2021-04-30', documentoIdentificacionArrendatario=2, codigoInmueble="alphaa2", valorPagado=500000)
        Pago.objects.create(
            fechaPago='2021-04-31', documentoIdentificacionArrendatario=1, codigoInmueble="alphaaa3", valorPagado=1000000)
    