from django.db import models

# Create your models here.

class Sample(models.Model):
    sample=models.AutoField(primary_key=True)
    sampleID=models.CharField(max_length=250, unique=True)
    samplingDate=models.DateField()
    viralLoad=models.DecimalField(decimal_places=5,max_digits=10)
    cd4=models.DecimalField(decimal_places=5,max_digits=10)
    
    gender=models.CharField(max_length=250)
    age=models.IntegerField()
    literacy=models.CharField(max_length=250)
    employment=models.CharField(max_length=250)
    riskFactors=models.CharField(max_length=250)
    maritalStatus=models.CharField(max_length=250)

    regimen=models.CharField(max_length=250)
    regimenStart=models.DateField()
    gender=models.CharField(max_length=250)
    gender=models.CharField(max_length=250)


