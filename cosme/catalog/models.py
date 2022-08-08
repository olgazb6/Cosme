from django.db import models

# Create your models here.


class Catalog(models.Model):
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=30)                                #категория
    product = models.CharField(max_length=30)                                 #тип
    image = models.ImageField(upload_to='catalog/static/catalog/img/')
    cost = models.DecimalField(max_digits=20, decimal_places=2)              #цена
    unit = models.CharField(max_length=10, blank=True, null=True)            #ед.измерения
    volume = models.FloatField()                                             #объем
    info = models.TextField()
    ingredients = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.name


