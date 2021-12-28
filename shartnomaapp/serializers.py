from .models import *
from rest_framework.serializers import *

class KursSerializer(ModelSerializer):
    class Meta:
        model = Kurs
        fields = ['nom', 'narx']
        