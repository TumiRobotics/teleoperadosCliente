from django.urls import path
from . import views

app_name = 'robotMovil'

urlpatterns = [
    path('index',views.index,name='index')
]