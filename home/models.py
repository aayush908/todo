from django.db import models

# Create your models here.
class event(models.Model):
     
    work = models.CharField(max_length=255)
    workdes = models.CharField(max_length=13)
    date = models.CharField(max_length=100)
    
    timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "event :  " + self.work