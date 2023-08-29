from django.shortcuts import render, redirect
from django.http import HttpResponse
from json import dumps
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from .models import *

from datetime import date as d

# Create your views here.
def index(request):
    return render(request, 'index.html')

def calculate(request):
    return render(request, 'calc.html')
def blog(request):
    return HttpResponse("this is blog page")
def result(request):
    lpg = request.POST.get("LPG")
    petrol = request.POST.get("Petrol")
    electricity = request.POST.get("electricity")
    diesel = request.POST.get("Diesel")
    
    cfc_lpg = int(float(lpg) * 2.80)
    cfc_petrol = int(float(petrol) * 2.32)
    cfc_electricity = int(float(electricity) * 0.69)
    cfc_diesel = int(float(diesel) * 2.70)

    cf_qty_lst = [cfc_lpg, cfc_petrol, cfc_electricity, cfc_diesel, 0]
    cf_name_lst = ['LPG', 'Petrol', 'Electricity', 'Diesel']
    total = sum (cf_qty_lst)

    ctx =  {'qty': cf_qty_lst, 'name': cf_name_lst, 'total': total}
    dataJson = dumps(ctx)

    if request.user.is_authenticated:
        user = request.user
        today = d.today()
        data, created = dailyData.objects.get_or_create(user = user, date = today )
        if not created:
            data.lpg = cfc_lpg
            data.petrol = cfc_petrol
            data.diesel = cfc_diesel
            data.electricity = cfc_electricity
            data.save()
        else:
            data.lpg = cfc_lpg
            data.petrol = cfc_petrol
            data.diesel = cfc_diesel
            data.electricity = cfc_electricity
            data.save()
    else:
        print('false')

    return render(request, 'result.html', {'data':dataJson})

def test(request):
    return render(request, 'loginLogout.html')

def login_button(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        pswd = request.POST.get('pswd')
        user  = authenticate(username = user_name, password = pswd)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return redirect('/')
    else:
        return HttpResponse('404 notfound')

def signin_button(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        pswd = request.POST['password']
        
        u = User.objects.create_user(username=username, email=email, password=pswd)
        # Rest of your logic
        login(request,username)
        return redirect('/')  # Redirect to the login page after successful signup
    return render(request, 'loginLogout.html')

def logout(request):
    return HttpResponse("this is logoutpage")

def Login_page(request):

    return render(request, 'loginLogout.html')


def loginLogoutPage(request):
    return HttpResponse("this is login logout page")