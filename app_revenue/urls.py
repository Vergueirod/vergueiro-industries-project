from django.urls import path
from . import views

app_name='app_revenue'

urlpatterns = [
    path('revenue/', views.registerRevenue, name='revenue'),
]