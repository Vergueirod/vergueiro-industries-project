from django.urls import path
from . import views

app_name='app_revenue'

urlpatterns = [
    path('revenue/', views.revenueCrud, name='revenue'),
    path('revenue/<int:id>', views.revenueCrud, name='revenue_item'),
    path('read-revenue/', views.readRevenue, name='read-revenue'),
]