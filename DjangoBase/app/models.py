from django.db import models

class Product(models.Model):
    reference  = models.CharField(max_length=255, unique=True, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    volume = models.FloatField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.reference 
