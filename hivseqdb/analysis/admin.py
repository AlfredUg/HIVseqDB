from django.contrib import admin
from analysis.models import NewAnalysis,AnalysisResults, MinorityVariantsResult
# Register your models here.
admin.site.register(NewAnalysis)
admin.site.register(AnalysisResults)
admin.site.register(MinorityVariantsResult)
