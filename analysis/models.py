from django.db import models
from django.urls import reverse
# Create your models here.

class NewAnalysis(models.Model):
    analysis_id=models.AutoField(primary_key=True)
    project_ID=models.CharField(max_length=250, default="PRJN00923")
    description=models.CharField(max_length=250, default="DTG virological failure adults in Uganda")
    email=models.EmailField(max_length=250)
    mutation_Database=models.CharField(max_length=250)
    consensus_Percentage=models.DecimalField(decimal_places=2,max_digits=5,default=20)
    target_Coverage=models.DecimalField(decimal_places=2,max_digits=5,default=10000) 
    length_Cutoff=models.DecimalField(decimal_places=2,max_digits=5,default=100) 
    score_Cutoff=models.DecimalField(decimal_places=2,max_digits=5,default=30) 
    error_Rate=models.DecimalField(decimal_places=2,max_digits=5,default=0) 
    minimum_Variant_Quality=models.DecimalField(decimal_places=2,max_digits=5,default=0.01) 
    minimum_Read_Depth=models.DecimalField(decimal_places=2,max_digits=5,default=100) 
    minimum_Allele_Count=models.DecimalField(decimal_places=2,max_digits=5,default=0.01) 
    minimum_Mutation_Frequency=models.DecimalField(decimal_places=2,max_digits=5,default=0.01) 

    def __str__(self):
        return self.project_ID
    def get_absolute_url(self):
        return reverse('newAnalysisForm')

class AnalysisResults(models.Model):
    analysis_results_id=models.AutoField(primary_key=True)
    sample_ID=models.CharField(max_length=250, default="S001")
    gene=models.CharField(max_length=250, default="IN")
    wildType=models.CharField(max_length=250, default="N")
    position=models.IntegerField(default=100)
    mutation=models.CharField(max_length=250, default="H")
    mutation_Frequency=models.DecimalField(decimal_places=2,max_digits=5,default=100)
    Consensus_sequence=models.CharField(max_length=250, default="ACGTGGGGGGGTCTGGGG")
    project_ID=models.ForeignKey('NewAnalysis', on_delete=models.CASCADE)

    def __str__(self):
        return self.sample_ID
    def get_absolute_url(self):
        return reverse('newAnalysisForm')
