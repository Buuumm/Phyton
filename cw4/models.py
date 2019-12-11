from django.db import models
from django.db.models import ForeignKey


class klient(models.Model):
    idklient = models.ForeignKey(auto,on_delete=models.PROTECT)
    nazwisko = models.CharField(max_length=45)
    login = models.CharField(max_length=45)
    haslo = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    nr_prawojazdy = models.CharField(max_length=45)



    def __str__(self):
        return self.login


class auto(models.Model):
    nr_placowy = models.ForeignKey(rezerwacja, on_delete=models.PROTECT)
    mark = models.CharField(max_length=45)
    model = models.CharField(max_length=45)
    rocznik = models.CharField(max_length=45)
    przebieg = models.IntegerField(default=0)


class rezerwacja(models.Model):
    idrezerwacja = models.IntegerField(primary_key=True)
    nr_placowy = models.IntegerField(primary_key=True)
    idklient = models.IntegerField(primary_key=True)
    data_wypozyczenia = models.DateTimeField(auto_now_add=True)
    data_zwrotu = models.DateTimeField(auto_now_add=True)
    cena = models.IntegerField(default=0)




class administrator(models.Model):
    idadministrator = models.IntegerField(primary_key=True)
    login = models.CharField(max_length=45)
    haslo = models.CharField(max_length=45)

