from django.db import models

# Create your models here.
class Details(models.Model):
    color = models.CharField(max_length=255)
    ram = models.IntegerField()
    memory = models.IntegerField()

    def __str__(self) -> str:
        return self.color
    

class Smartphones(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    price = models.FloatField()
    img_url = models.CharField(max_length=255, default="no image")
    details = models.OneToOneField('Details', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name