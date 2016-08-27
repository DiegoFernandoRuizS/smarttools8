from django.db import models

# Create your models here.

class Usuario(models.Model):
    name = models.CharField(max_length=200, null=False)
    surname = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=200, null=False)
    password = models.CharField(max_length=200, null=False)
    rol = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
