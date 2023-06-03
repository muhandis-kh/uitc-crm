from django.db import models
from autoslug import AutoSlugField
    
from userapp.models import Student
from mainapp.models import Branch, Group


MONTH_NAME = (
        ('yan', "Yanvar"),
        ('fev', "Fevral"),
        ('mar', "Mart"),
        ('apr', "Aprel"),
        ('may', "May"),
        ('iyn', "Iyun"),
        ('iyl', "Iyul"),
        ('avg', "Avgust"),
        ('sen', "Sen"),
        ('okt', "Oktyabr"),
        ('noy', "Noyabr"),
        ('dek', "Dekabr"),
    )

# Create your models here.

class Expenses(models.Model):
    """ Harajatlar modeli """
    name = models.CharField(max_length=250, verbose_name="Harajat nomi")
    slug  = AutoSlugField(populate_from="name", unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Miqdori")
    comment = models.TextField(verbose_name="Izoh")
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name="expenses", verbose_name="Filial")

    status = models.BooleanField(default=True, verbose_name="Holati")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Harajat"
        verbose_name_plural = "Harajatlar"
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

class Payment(models.Model):
    """ O'quvchining to'lov qilishi un model """
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='payments', verbose_name="Filial")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="payments", verbose_name="gruhi")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="payments", verbose_name="O'quvchi")
    month = models.CharField(max_length=25, choices=MONTH_NAME, verbose_name="Oylar")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Miqdori")

    status = models.BooleanField(default=True, verbose_name="Holati")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "To'lov"
        verbose_name_plural = "To'lovlar"
        ordering = ('-created_at',)

    def __str__(self):
        text = f"{self.student.full_name} - {self.month}"
        return text
  
class Area(models.Model):
    """ Kompaniyaning xizmat ko'rsatish turlari uchun model """
    name  = models.CharField(max_length=250, verbose_name="Nomi")
    slug  = AutoSlugField(populate_from="name", unique=True)

    status = models.BooleanField(default=True, verbose_name="Holati")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Hizmat"
        verbose_name_plural = "Hizmatlar"
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

class Income(models.Model): 
    """ Daromadlar uchun model """
    name  = models.CharField(max_length=250, verbose_name="Nomi")
    slug  = AutoSlugField(populate_from="name", unique=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='incoms', verbose_name="Filial")
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='incoms', verbose_name="Xizmat turi")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Miqdori")
    comment = models.TextField(verbose_name="Izoh")
    
    status = models.BooleanField(default=True, verbose_name="Holati")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Daromad"
        verbose_name_plural = "Daromadlar"
        ordering = ('-created_at',)

    def __str__(self):
        return self.name


