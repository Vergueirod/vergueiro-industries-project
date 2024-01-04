from django.urls import path
from . import views

app_name='app_revenue'

urlpatterns = [
    path('revenue/', views.revenueCrud, name='revenue'),
    path('read-revenue/', views.readRevenue, name='read-revenue'),
]