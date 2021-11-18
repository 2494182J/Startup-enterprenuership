from django.urls import path
from enterprenuership import views


app_name = 'enterprenuership'

urlpatterns = [
path('', views.index, name='index'),
]