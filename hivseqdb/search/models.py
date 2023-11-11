from django.db import models
from django.utils import timezone

# Create your models here.

class Sample(models.Model):
    sample_id=models.AutoField(primary_key=True)
    sampleName=models.CharField(max_length=250)
    gender=models.CharField(max_length=250)
    location=models.CharField(max_length=250)
    age=models.IntegerField()
    regimen=models.CharField(max_length=250)
    viralLoad=models.DecimalField(decimal_places=2,max_digits=5,default=100)
    samplingDate=models.DateField(default=timezone.now)

    def __str__(self):
        return self.sampleName
    def get_absolute_url(self):
        return reverse('searchsample')
