
# RestFramework Django
from rest_framework import serializers
from .models import Pago

class PagoSerializer(serializers.ModelSerializer):
    ''' This Claas will select all the fields of the model structure and
     Serialize the data from Json format to Python object and viceversa'''
    class Meta:
        model = Pago
        fields = '__all__'