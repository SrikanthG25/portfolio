from django.urls import path
from .views import *

urlpatterns = [
path('', index, name='index'),
path('message/', MessageData.as_view(), name='index'),
]
