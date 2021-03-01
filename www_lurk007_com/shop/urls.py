from django.urls import path
from .views import *

app_name = 'shop'
urlpatterns = [
    path('add/', add, name='add'),
    path('get/', get, name='get'),
    path('', login, name='login'),
    path('index/', index, name='index'),
    path('check_login/', check_login, name='check_login'),
]

