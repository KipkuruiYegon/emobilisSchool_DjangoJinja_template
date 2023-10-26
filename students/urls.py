# give every app default path
# one project path, one app path urls



from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('contact', views.contact),
    path('classes', views.classes)
]