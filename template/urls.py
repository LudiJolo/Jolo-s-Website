from django.urls import path
from . import views

app_name = 'template'
#stores all urls that are associated with the app
urlpatterns = [
    path('', views.index, name='index'),
]