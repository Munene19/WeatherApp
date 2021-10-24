from django.urls import path
from . import views

urlpatterns = [
    path('datalist/', views.dataList, name="data-list"),
]