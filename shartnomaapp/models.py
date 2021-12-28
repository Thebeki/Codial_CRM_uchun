from django.db import models

class Kurs(models.Model):
    nom = models.CharField(max_length=30)
    narx = models.IntegerField()
    def str(self):
        return self.nom

class Ustoz(models.Model):
    ism = models.CharField(max_length=30)
    yosh = models.PositiveSmallIntegerField()
    tel = models.CharField(max_length=30, blank=True)
    def str(self):
        return self.ism

class Student(models.Model):
    ism = models.CharField(max_length=30)
    familiya = models.CharField(max_length=30)
    sharif = models.CharField(max_length=30, blank=True)
    jins = models.CharField(max_length=7, choices=(("o'g'il", "o'g'il"), ("qiz", "qiz")))
    tel1 = models.CharField(max_length=15)
    tel2 = models.CharField(max_length=15, blank=True)
    status = models.CharField(max_length=15, choices=(("new", "new"), ("loyal", "loyal")))
    def str(self):
        return f"{self.ism} {self.familiya}"

class Shartnoma(models.Model):
    K = (
        ("08:00-10:00", "08:00-10:00"),
        ("10:00-12:00", "10:00-12:00"),
        ("14:00-16:00", "14:00-16:00"),
        ("16:00-18:00", "16:00-18:00"),
        ("18:00-20:00", "18:00-20:00"),
    )
    shartnoma_raqami = models.PositiveSmallIntegerField()
    student = models.ForeignKey(Student, on_delete=models.SET_NULL)
    kurs = models.ForeignKey(Kurs, on_delete=models.SET_NULL)
    ustoz = models.ForeignKey(Ustoz, on_delete=models.SET_NULL)
    kunlari = models.CharField(max_length=30, choices=(("Dushanba-Juma", "Dushanba-Juma"), ("Seshanba-Shanba","Seshanba-Shanba")))
    kurs_vaqti = models.CharField(max_length=30, choices=K)
    guruh_nomi = models.CharField(max_length=30)
    tuzuvchi = models.CharField(max_length=30)
    sinov_dars_sanasi = models.DateField()
    status = models.CharField(max_length=15, choices=(("Active", "Active"), ("Passive", "Passive")))
    
    def str(self):
        return f"#{self.shartnoma_raqami} {self.student.ism} ({self.status}) {self.kurs.nom}"