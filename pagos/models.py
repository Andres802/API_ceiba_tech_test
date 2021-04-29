from django.db import models
from django.contrib.auth import get_user_model

#validators
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

class Pago(models.Model):
    '''This Pago class is will build the database structure in our MYSQL database'''
    fechaPago = models.DateField()
    documentoIdentificacionArrendatario = models.IntegerField(primary_key=True, null=False)
    codigoInmueble = models.CharField(unique=True, max_length=50, null=False, validators=[alphanumeric])
    valorPagado = models.IntegerField(default=1, validators=[MaxValueValidator(1000000), MinValueValidator(1)])

    class Meta:
        '''
        This Class set table name in MySql Database
        '''
        db_table = "pagos"
