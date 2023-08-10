from django.contrib import admin
from django.urls import path
from report.views import drug_report_page, DrugResistanceView

urlpatterns = [
    path('tools/generate-drug-resistance-report/', DrugResistanceView.as_view(), name='reportInput'),
    path('tools/drug-resistance-report/', drug_report_page, name='reportResult'),
]
