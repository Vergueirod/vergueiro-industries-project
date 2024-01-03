from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from app_expenditure.models import Expenditure
from app_revenue.models import Revenue


# Get my cost total 
@login_required(login_url='/auth/login')
def costTotal(request, month=None, year=None):

    queryset = Expenditure.objects.all()

    if month and year:
        queryset = queryset.filter(month=month, year=year)
    
    total_cost = sum(values.value for values in queryset)
    return total_cost

# Get my revenue total
@login_required(login_url='/auth/login')
def revenueTotal(request, month=None, year=None ):

    queryset = Revenue.objects.all()

    if month and year:
        queryset = queryset.filter(month=month, year=year)
    
    total_revenue = sum(values.value_revenue for values in queryset)
    return total_revenue

# Balance view
@login_required(login_url='/auth/login')
def myBalance(request):

    total_revenue = revenueTotal(request)
    total_cost = costTotal(request)

    my_balance_general = total_revenue - total_cost

    month = request.GET.get('month')
    year = request.GET.get('year')

    if month and year:
        total_revenue = revenueTotal(request, month, year)
        total_cost = costTotal(request, month, year)
        my_balance_general = total_revenue - total_cost

        print(f"{my_balance_general}")

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
        'months_choices': MONTHS_CHOICES, 
    }
    
    return render(request, 'home/home.html', context)

# Principles for life
@login_required(login_url='/auth/login')
def myPrinciples(request):
    return render(request, 'principles/principles.html')