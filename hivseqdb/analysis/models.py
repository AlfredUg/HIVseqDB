from django.db import models
from django.urls import reverse
# Create your models here.

class NewAnalysis(models.Model):
    analysis_id=models.AutoField(primary_key=True)
    project_ID=models.CharField(max_length=250, unique=True)
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
    sample_ID=models.CharField(max_length=250)
    drugClass=models.CharField(max_length=250,null=True, blank=True)
    drugName=models.CharField(max_length=250,null=True, blank=True)
    drugScore=models.DecimalField(decimal_places=2,max_digits=5,null=True, blank=True)
    susceptibility=models.CharField(max_length=250,null=True, blank=True)
    project_ID=models.CharField(max_length=250,null=True, blank=True)
    #project_ID=models.ForeignKey(NewAnalysis, to_field="project_ID",db_column="project_ID",on_delete=models.CASCADE)

    def __str__(self):
        return self.sample_ID
    def get_absolute_url(self):
        return reverse('newAnalysisForm')

class MinorityVariantsResult(models.Model):
    result=models.AutoField(primary_key=True)
    chromosome=models.CharField(max_length=250)
    gene=models.CharField(max_length=250,null=True, blank=True)
    category=models.CharField(max_length=250,null=True, blank=True)
    surveillance=models.CharField(max_length=250,null=True, blank=True)
    wildtype=models.CharField(max_length=250,null=True, blank=True)
    position=models.IntegerField()
    mutation=models.CharField(max_length=250,null=True, blank=True)
    mutation_frequency=models.DecimalField(decimal_places=2,max_digits=10,null=True, blank=True)
    coverage=models.DecimalField(decimal_places=2,max_digits=10,null=True, blank=True)
    sample=models.CharField(max_length=250,null=True, blank=True)
    project=models.CharField(max_length=250,null=True, blank=True)
    #project_ID=models.ForeignKey(NewAnalysis, to_field="project_ID",db_column="project_ID",on_delete=models.CASCADE)

    def __str__(self):
        return self.project
    def get_absolute_url(self):
        return reverse('newAnalysisForm')
