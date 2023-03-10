from django.db import models
from asosiy.models import Mahsulot
from userapp.models import Profil

class Savat(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    umumiy = models.PositiveSmallIntegerField()
    miqdor = models.PositiveSmallIntegerField(default=1)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)

class Tanlangan(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)

