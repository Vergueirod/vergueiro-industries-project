from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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


# Get my revenue total
@login_required(login_url='/auth/login')
def revenueTotal(request):
    revenue_total = Revenue.objects.values_list('value_revenue', flat=True)
    total_revenue = 0
    
    for values in revenue_total :
        total_revenue += values
    return total_revenue


# Salary total
@login_required(login_url='/auth/login')
def salaryTotal(request):
    salary_total = Revenue.objects.filter(revenue_types__iexact='SAL').values_list('value_revenue', flat=True)

    total_salary = 0
    for values in salary_total:
        total_salary += values
    return total_salary


# Benefits total
@login_required(login_url='/auth/login')
def benefitsTotal(request):

    benefits_total = Revenue.objects.filter(revenue_types='BEN').values_list('value_revenue', flat=True)
    total_benefits = 0 

    for values in benefits_total:
        total_benefits += values
    return total_benefits


# Balance view
@login_required(login_url='/auth/login')
def myBalance(request):

    total_revenue = revenueTotal(request)
    total_cost = costTotal(request)
    total_salary = salaryTotal(request)
    total_benefits = benefitsTotal(request)

    my_balance_live =  total_salary - total_cost
    my_balance_general = total_revenue - total_cost

    MONTHS_CHOICES = [
            (1, 'January'),
            (2, 'February'),
            (3, 'March'),
            (4, 'April'),
            (5, 'May'),
            (6, 'June'),
            (7, 'July'),
            (8, 'August'),
            (9, 'September'),
            (10, 'October'),
            (11, 'November'),
            (12, 'December'),
        ]

    context = {
        'total_revenue': total_revenue,
        'total_cost': total_cost,
        'my_balance_general': my_balance_general,
        'my_balance_live': my_balance_live,
        'total_salary': total_salary,
        'total_benefits': total_benefits,
        'months_choices': MONTHS_CHOICES, 
    }
    
    return render(request, 'home/home.html', context)

# Principles for life
@login_required(login_url='/auth/login')
def myPrinciples(request):
    return render(request, 'principles/principles.html')