from django.shortcuts import render
from django.contrib import messages

# Create your views here.

def home(request):
    messages.info(request,'Welcome to HIVseqDB, store data, analyse data, browse data and analyses.')
    # messages.warning(request,
    # 'This instance only allows browsing of already analysed data. '+
    # 'To upload and analyse own data, kindly install an instance as indicated in the documentation.')

    return render(request, 'base/home.html')

def login(request):
    return render(request, 'base/login.html')