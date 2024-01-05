from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Revenue
from django.http import JsonResponse


# Read data in table:
@login_required(login_url='/auth/login')
def readRevenue(request):
    if request.method == 'GET':
        read_test = Revenue.objects.all()
    return JsonResponse({'revenues': list(read_test.values())})


# Revenue register
@login_required(login_url='/auth/login')
def revenueCrud(request, id=None):
    if request.method == 'GET':
        revenues = Revenue.objects.all()
        
        context = {
            'revenues' : revenues,
        }
        return render(request, 'revenue/revenue.html', context)
    elif request.method == 'DELETE':
        print('teste')
        try:
            item = Revenue.objects.get(id=id)
            item.delete()
            return JsonResponse({'status': 'success'})

        except Revenue.DoesNotExist:
            return JsonResponse({'status': 'error'}, status=404)
        
    
    '''
    if request.method == 'GET': # READ
        context = {
            'revenues' : Revenue.REVENUE_TYPES_CHOICES,
            'months' : Revenue.MONTHS_CHOICES,
            'years' : Revenue.year,
            'values' : Revenue.value_revenue,
        }
        return render(request, 'revenue/revenue.html', context)
    
    elif request.method == 'POST': # CREATE
        
        revenue_choice = request.POST.get('revenue')
        value = request.POST.get('value')
        month = request.POST.get('month')
        year = request.POST.get('year')

        revenue = Revenue(
            revenue_types = revenue_choice,
            value_revenue = value,
            month = month,
            year = year
        )

        revenue.save()
        return HttpResponse('Dados salvos com sucesso!')
'''
