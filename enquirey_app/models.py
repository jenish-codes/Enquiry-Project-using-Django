from django.db import models

class Enquiry(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    message = models.CharField(max_length=300)