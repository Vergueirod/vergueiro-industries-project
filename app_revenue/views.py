from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Revenue

'''
1. Crio a funcão
2. crio a condicional 
    a) GET: Vou trazer o que quero que ele mostre sempre (Campos para preencher)
    b) POST: Coletar os dados em uma variavel para enviar para o DB
3. Cria uma nova instância
4. Salvo no banco
'''
# Create your views here.

@login_required(login_url='/auth/login')
def registerRevenue(request):
    if request.method == 'GET':
        
        context = {

            'revenues' : Revenue.REVENUE_TYPES_CHOICES,
            'months' : Revenue.MONTHS_CHOICES,
            'years' : Revenue.year,
            'values' : Revenue.value_revenue,

        }

        return render(request, 'revenue/revenue.html', context)
    
    elif request.method == 'POST':

        revenue_choice = request.POST.get('revenue')
        value = request.POST.get('value')
        month = request.POST.get('month')
        year = request.POST.get('year')

        print(revenue_choice, value, month, year)

        revenue = Revenue(

            revenue_types = revenue_choice,
            value_revenue = value,
            month = month,
            year = year

        )

        revenue.save()

        return HttpResponse('Dados salvos com sucesso!')