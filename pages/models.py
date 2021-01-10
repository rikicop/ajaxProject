from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        template = '{0.name} {0.cargo} {0.email}'
        return template.format(self)  



    
class Sum(models.Model):
    first = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=False)
    second = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=False)


    def __str__(self):
        return str(self.first)
