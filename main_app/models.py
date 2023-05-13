from django.db import models
from autoslug import AutoSlugField
# Create your models here.
class Branch(models.Model):
    """ Branch - ushbu model filiallar uchun yaratilgan va loyihani """

    name = models.CharField(max_length=100, unique=True, verbose_name="Nomi")
    slug = AutoSlugField(populate_from='name', unique=True)
    address = models.CharField(max_length=250, verbose_name="Manzil")
    
    status = models.BooleanField(default=True, verbose_name="Holati")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Filiallar"
        ordering = ("-created_at", )
        
    def __str__(self):
        return self.name
    
class Field(models.Model):
    """ Fields modeli = o'quv markazdagi yo'nalishlarni aniqlash uchun yaratilgan"""
    
    name = models.CharField(max_length=100, unique=True, verbose_name="Nomi")
    slug = AutoSlugField(populate_from='name', unique=True)
    cost = models.DecimalField(max_digits=8, decimal_places=2, default=100000, blank=True, null=True, verbose_name="Kurs narxi")
    duration = models.PositiveIntegerField(default=1, verbose_name="Kurs davomiyligi")
    
    status = models.BooleanField(default=True, verbose_name="Holati")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"
        ordering = ("-created_at", )
        
    def __str__(self):
        return self.name


def slugify_two_fields(self):
        return "{}-{}".format(self.branch.name, self.number)

class Room(models.Model):
    """ Room modeli = o'quv markazdagi xonalar uchun yaratilgan"""
    
    number = models.PositiveIntegerField(verbose_name="Xona raqami", default=1)
    # slug = AutoSlugField(populate_name=number, unique=True)
    slug = AutoSlugField(
        (u'slug'),
        populate_from=slugify_two_fields, unique=True
    )
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, verbose_name="Filial", related_name='rooms')
    capacity = models.PositiveIntegerField(default=8, verbose_name="Xona sig'imi")
    
    status = models.BooleanField(default=True, verbose_name="Holati")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Xona"
        verbose_name_plural = "Xonalar"
        ordering = ("-created_at", )
        
    def __str__(self):
        text = f"{self.branch.name} / {self.number}-xona"
        return text
    