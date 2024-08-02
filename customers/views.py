from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . models import Customer

# Create your views here.
def show_account(request):
    if request.POST and 'register' in request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        # create user accounts
        user=User.objects.create(
            username=username,
            password=password,
            email=email
        )
        # create customer accounts
        customer=Customer.objects.create(
            user=user,
            phone=phone,
            address=address
        )
        return redirect('home')

    return render(request,'account.html')
