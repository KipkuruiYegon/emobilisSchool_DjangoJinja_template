from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.

# all functions shall be defined here
def home(request):
    return render(request, 'homeB.html')
