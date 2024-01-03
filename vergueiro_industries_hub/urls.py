from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('app_auth.urls')),
    path('app1/', include('app_home.urls', namespace='app_home')),
    path('app2/', include('app_revenue.urls', namespace='app_revenue')),
    path('app3/', include('app_expenditure.urls', namespace='app_expenditure')),
]
