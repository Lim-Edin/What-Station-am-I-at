from . import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from .views import SubwayListView

urlpatterns = [
    path('', views.subway, name='subway'),
    path('subway', SubwayListView.as_view(), name='subway'),
    path('select', views.select, name='select')
]