from django.shortcuts import render
from rest_framework import generics
from .models import *
from CRM.shartnomaapp.serializers import *

class KursListAPIView(generics.ListCreatAPIView):
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer

class UstozListAPIView(generics.ListAPIView):
    queryset = Ustoz.objects.all()
    serializer_class = UstozSerializer

class StudentListAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ShartnomaListAPIView(generics.ListAPIView):
    queryset = Shartnoma.objects.all()
    serializer_class = StudentSerializer

