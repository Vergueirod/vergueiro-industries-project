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


'''
@login_required(login_url='/auth/login')
def home(request):
    return render(request, 'home/home.html')


@login_required(login_url='/auth/login')
def expenditureDataShow(request):   
    expenditures = Expenditure.objects.all().order_by('-year', '-month')  # Get all revenue objects, ordered by year and month
    get_value = Expenditure.objects.values_list('value', flat=True)

    total_price = 0
    for i in get_value:
        total_price += i

    november_revenue = 5650
    delta = november_revenue - total_price
        
    return render(request, 'home/home.html', {
                                                'expenditures': expenditures,
                                                'total_price': total_price,
                                                'november_revenue': november_revenue,
                                                'delta': delta,
                                                
                                                })



def requestExams(request):
    exams_type = TiposExames.objects.all()

    if request.method == 'GET':
        return render(request, 'request/request.html', {'exams_type' : exams_type})
    elif request.method == 'POST':
            opt_exams = request.POST.getlist('exams') # Pega os dados do usuario
            request_exams = TiposExames.objects.filter(id__in=opt_exams) # consulta os dados no banco
            valitation = TiposExames.objects.filter(id__in=opt_exams, disponivel=True)
            
            preco_total = 0
            for i in valitation: # realiza a query
                 preco_total +=  i.preco

            return render(request, 'request/request.html', {'exams_type' : exams_type, # Libera os dados para o front consumir
                                                            'request_exams': request_exams,
                                                            'preco_total': preco_total ,})

# Create your views here.
#@login_required(login_url='/auth/login')
#def home(request):
#    return render(request, 'home/home.html')

@login_required(login_url='/auth/login')
def home(request):
    expenditures = Expenditure.objects.all().order_by('-year', '-month')  # Get all expenditure objects, ordered by year and month
    return render(request, 'home/home.html', {'expenditures': expenditures})


@login_required(login_url='/auth/login')
def home(request):
    revenues = Revenue.objects.all().order_by('-year', '-month')  # Get all revenue objects, ordered by year and month
    expenditures = Expenditure.objects.all().order_by('-year', '-month')  # Get all expenditure objects, ordered by year and month
    context = {
        'revenues': revenues,
        'expenditures': expenditures
    }
    return render(request, 'home/home.html', context)

'''
