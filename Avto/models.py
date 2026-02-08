from django.db import models

class IshTuri(models.Model):
    nomi = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nomi or "No Name"



class Usta(models.Model):
    ism = models.CharField(max_length=100)
    tajriba_yil = models.PositiveIntegerField()
    ishlar = models.ManyToManyField(IshTuri)  # Bu many-to-many
    telefon = models.CharField(max_length=20)
    shahar = models.CharField(max_length=50, null=True)
    yoshi = models.IntegerField(null=True)

    def __str__(self):
        return self.ism
