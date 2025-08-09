from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length= 30)
    phone = models.CharField(max_length= 12)
    email = models.CharField(max_length= 45)
    desc = models.TextField(max_length= 122)
    sign= models.FileField(upload_to='', blank = True,null = True)
    hear = models.TextField(max_length= 122,null = True)

    def __str__(self):
        return self.name

# Create your models here.
