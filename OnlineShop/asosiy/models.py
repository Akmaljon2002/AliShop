from django.db import models
from userapp.models import *

# from OnlineShop.userapp.models import Profil


class Bolim(models.Model):
    nom = models.CharField(max_length=100)
    rasm = models.FileField(upload_to='bolimlar')
    def __str__(self):
        return self.nom

class Mahsulot(models.Model):
    nom = models.CharField(max_length=100)
    brend = models.CharField(max_length=100)
    narx = models.FloatField()
    davlat = models.CharField(max_length=50)
    chegirma = models.PositiveSmallIntegerField(default=0)
    yetkazish = models.CharField(max_length=50)
    kafolat = models.CharField(max_length=50)
    mavjud = models.BooleanField(default=True)
    tasdiqlangan = models.BooleanField(default=True)
    min_miqdor = models.PositiveSmallIntegerField(default=1)
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nom}, {self.brend}"

class Media(models.Model):
    rasm = models.FileField(upload_to='mahsulotlar')
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)

class Izoh(models.Model):
    baho = models.PositiveSmallIntegerField()
    matn = models.CharField(max_length=300)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    sana = models.DateField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return self.matn
