# from . import views
from django.urls import path
from .views import SubwayListView
from django.conf.urls import url
# from django.contrib import admin

urlpatterns = [
    path('', SubwayListView.as_view(), name='subway'),
]