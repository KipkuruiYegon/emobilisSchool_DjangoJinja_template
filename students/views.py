from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.

# all functions shall be defined here
def home(request):
    return render(request, 'homeB.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def classes(request):
    return render(request, 'classes.html')