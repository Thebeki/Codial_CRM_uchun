from django.db import models
from django.db.models.deletion import SET_NULL
from shartnomaapp.models import *
from .models import *

class Tolov(models.Model):
    shartnoma = models.ForeignKey(Shartnoma, on_delete=models.SET_NULL)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL)
    ustoz = models.ForeignKey(Ustoz, on_delete=models.SET_NULL)
    years = ( 
    ("2022", "2022"), 
    ("2023", "2023"), 
    ("2024", "2024"), 
    ("2025", "2025"),
    ) 

    months = ( 
    ("January", "January"), 
    ("February", "February"), 
    ("March", "March"), 
    ("April", "April"), 
    ("May", "May"), 
    ("June", "June"), 
    ("Jule", "Jule"), 
    ("August", "August"), 
    ("September", "September"), 
    ("October", "October"), 
    ("November", "November"), 
    ("December", "December"),  
    )
    kurs = models.ForeignKey(Kurs, on_delete=models.SET_NULL)
    yil = models.IntegerField(choices=years)
    tolov_oyi = models.CharField(choices=months)
    chegirma_status = models.CharField(default="Yo'q")
    chegirma_sababi = models.CharField()
    chegirma_miqdori= models.PositiveIntegerField()
    tolov_sanasi = models.DateField()
    kassir = models.CharField()
    tolash_lozim = models.PositiveIntegerField()
    naqd = models.PositiveIntegerField()
    bank = models.PositiveIntegerField()
    plastik = models.PositiveIntegerField()
    click = models.PositiveIntegerField()
    jami_toladi = models.PositiveIntegerField()
    jami_qoldi = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.ism} {self.familiya} ({self.jami_toladi})"
