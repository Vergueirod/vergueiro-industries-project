from django.urls import path
from . import views

app_name='app_expenditure'

urlpatterns = [
    path('expenditure/', views.expenditureData, name='expenditure'),
]

