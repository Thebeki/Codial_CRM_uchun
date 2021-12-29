from .models import *
from rest_framework.serializers import *

class KursSerializer(ModelSerializer):
    class Meta:
        model = Kurs
        fields = ['nom', 'narx']

class UstozSerializer(ModelSerializer):
    class Meta:
        model = Ustoz
        fields = ['ism', 'yosh']

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['ism', 'familiya']

class ShartnomaSerializer(ModelSerializer):
    class Meta:
        model = Shartnoma
        fields = ['student', 'kurs']