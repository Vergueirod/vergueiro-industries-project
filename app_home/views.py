from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#from .models import Revenue, Expenditure
from django.http import HttpResponse, HttpResponseRedirect
from app_expenditure.models import Expenditure
from app_revenue.models import Revenue


# Get my cost total 
@login_required(login_url='/auth/login')
def costTotal(request):
    cost_total = Expenditure.objects.values_list('value', flat=True)

    total_cost = 0
    for values in cost_total :

        total_cost += values

    return total_cost

    #print(total)
    #return render(request, 'home/home.html')

# Get my revenue total
@login_required(login_url='/auth/login')
def revenueTotal(request):
    revenue_total = Revenue.objects.values_list('value_revenue', flat=True)
    #others_total = Revenue.objects.filter(revenue_types='others').values_list('value_revenue', flat=True)

    total_revenue = 0
    for values in revenue_total :

        total_revenue += values
    
    return total_revenue

    #print(total)
    #return render(request, 'home/home.html')

@login_required(login_url='/auth/login')
def salaryTotal(request):
    salary_total = Revenue.objects.filter(revenue_types__iexact='SAL').values_list('value_revenue', flat=True)
    #total_salary = sum(salary_total)
    total_salary = 0
    for values in salary_total:
        total_salary += values
    return total_salary
    #print(total_salary)
    #return render(request, 'home/home.html')

@login_required(login_url='/auth/login')
def benefitsTotal(request):
    benefits_total = Revenue.objects.filter(revenue_types='BEN').values_list('value_revenue', flat=True)
    #total_benefits = sum(benefits_total)
    total_benefits = 0 
    for values in benefits_total:
        total_benefits += values
    return total_benefits
    #print(total_benefits)
    #return render(request, 'home/home.html')
    
# Make my balance (Revenue - Cost)
@login_required(login_url='/auth/login')
def myBalance(request):

    total_revenue = revenueTotal(request)
    total_cost = costTotal(request)
    total_salary = salaryTotal(request)
    total_benefits = benefitsTotal(request)

    my_balance_live =  total_salary - total_cost
    my_balance_general = total_revenue - total_cost

    context = {

        'total_revenue': total_revenue,
        'total_cost': total_cost,
        'my_balance_general': my_balance_general,
        'my_balance_live': my_balance_live,
        'total_salary': total_salary,
        'total_benefits': total_benefits,


    }
    
    return render(request, 'home/home.html', context)

def myPrinciples(request):
    return render(request, 'principles/principles.html')