from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Expenditure


# Expenditure JSON
@login_required(login_url='/auth/login')
def expenditureJson(request):
    expenditure_json = Expenditure.objects.all()
    return JsonResponse({'expenditures': list(expenditure_json.values())})


# Expenditure data
@login_required(login_url='/auth/login')
def expenditureData(request):
    if request.method == 'GET':
        
        expenditure_data = Expenditure.objects.all()

        context = {
            'expenditures': expenditure_data,
            'categories': Expenditure.CATEGORY_CHOICES,
            'payments': Expenditure.PAYMENT_METHOD_CHOICES,
            'months': Expenditure.MONTHS_CHOICES,
        }
        return render(request, 'expenditure/expenditure.html', context)
    
    elif request.method == 'POST':
       category_choice = request.POST.get('category')
       payment_choice = request.POST.get('payment')
       credit = request.POST.get('credit')
       month_choice = request.POST.get('month')
       year = request.POST.get('year')
       title = request.POST.get('title')
       value = request.POST.get('value')

       print(category_choice, payment_choice, credit, month_choice, year, title, value)
              
        # Cria uma nova instância do modelo Expenditure
       expenditure = Expenditure(
           category=category_choice,
           payment_method=payment_choice,
           credit_card=credit,
           month=month_choice,
           year=year,
           title=title,
           value=value
       )

       # Salva a instância no banco de dados
       expenditure.save()

       return HttpResponse('Dados salvos com sucesso!')