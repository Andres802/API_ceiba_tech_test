from django.test import TestCase, Client
from django.urls import reverse
from pagos.models import Pago
import json

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.pago_url = reverse('pago')
        self.pago1 = Pago.objects.create(
            fechaPago= "2021-03-29",
            documentoIdentificacionArrendatario= "971203",
            codigoInmueble= "unitest1",
            valorPagado= "70000"
        )
    
    def test_pago_arriendo_GET(self):
        
        response = self.client.get(self.pago_url)
        self.assertEquals(response.status_code, 200)
    
    def test_pago_arriendo_POST_add_new_pago(self):
        
        self.pago1,

        response = self.client.post(self.pago_url, {
            "fechaPago": "2021-03-29",
            "documentoIdentificacionArrendatario": "971203",
            "codigoInmueble": "unitest1",
            "valorPagado": "70000" 
        })
        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.pago1.codigoInmueble, 'unitest1')

