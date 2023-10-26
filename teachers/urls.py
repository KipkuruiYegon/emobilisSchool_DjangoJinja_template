# give every app default path
# one project path, one app path urls



from django.urls import path
from . import views


app_name = "teachers"
urlpatterns = [
    path('', views.home),
]