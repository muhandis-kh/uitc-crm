from django.db import models
from main_app.models import Field
from django.core.validators import RegexValidator

# Create your models here.

_validate_phone = RegexValidator(
    regex=r"^[\+]?[(]?[8-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$",
    message="Telefon raqamingiz + yoki 9 bilan boshlanishi va 12 belgidan oshmasligi lozim. Masalan: +998991271405",
)

DAYS = (
    ("toq", "Du-Chor-Jum"),
    ("juft", "Se-Pay-Shan"),
    ("boot", "Bootcamp"),
) 

TIME = (
    ('8', "8:00-11:00"),
    ('12', "12:00-14:00"),
    ('14', "14:00-17:00"),
    ('17', "17:00-20:00"),
) 
class Role(models.Model):
    """ Xodimlarning vazifasini yaratuvchi model """
    name = models.CharField(max_length=250, verbose_name="Vazifasi")
    
    status = models.BooleanField(default=True, verbose_name="Holati")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class Worker(models.Model):
    """ Xodimlar yaratish uchun model """
    
    full_name = models.CharField(max_length=255, verbose_name="Ism Familiyasi")
    role = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name="Vazifasi", related_name="workers")
    phone_number = models.CharField(max_length=18, validators=[_validate_phone], verbose_name="Telefon raqami", unique=True)
    passport = models.CharField(max_length=15, verbose_name="Passport raqami", unique=True)
    direction = models.ForeignKey(Field, on_delete=models.CASCADE, verbose_name="O'qituvchi yo'nalishi", related_name='workers')
    percentage = models.PositiveIntegerField(verbose_name="O'qituvchi foizi", blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Maosh", blank=True, null=True)
    
    status = models.BooleanField(default=True, verbose_name="Holati")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Xodim"
        verbose_name_plural = "Xodimlar"
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.full_name


class Student(models.Model):
    """ O'quvchi yaratish uchun model """
    full_name = models.CharField(max_length=100, verbose_name="Ism va Familyasi")
    date_of_birth = models.DateField(verbose_name="Tug'ilgan sanasi")
    passport = models.CharField(max_length=15, verbose_name="Passport raqami", unique=True)
    phone_number = models.CharField(max_length=18, validators=[_validate_phone], verbose_name="Telefon raqami", unique=True)
    parents_name = models.CharField(max_length=100, verbose_name="Ota-onasining ismi")
    parents_phone_number = models.CharField(max_length=18, validators=[_validate_phone], verbose_name="Ota-onasining telefon raqami", unique=True)
    field = models.ForeignKey(Field, on_delete=models.CASCADE, verbose_name="Yo'nalish", related_name='students')
    day = models.CharField(max_length=25, choices=DAYS, default='toq', verbose_name="Kurs kunlari")
    time = models.CharField(max_length=25, choices=TIME, default='8', verbose_name="Kurs vaqtlari")
    
    status = models.BooleanField(default=True, verbose_name="Holati")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "O'quvchi"
        verbose_name_plural = "O'quvchilar"
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.full_name

    

