from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,  redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required


# login validation
def login_auth(request):
   if request.method == 'GET':
      return render(request, 'login/login.html')

   username = request.POST.get('username')
   password = request.POST.get('password')

   user = authenticate(username=username, password=password)
   print(user)

   if user:
      django_login(request, user)
      return redirect('app_home:dashboard')
   
   return render(request, 'login/login.html')

