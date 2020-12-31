from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from users.forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib import messages



def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get('email')
            if not email.endswith('@ietdavv.edu.in'):
                messages.error(request,'Please use student email provided by college')
                return render(request, 'users/register.html', {'form': form})
            if User.objects.filter(email=form.cleaned_data.get('email')).exists():
                messages.info(request,'Student already registered with these id')
                return render(request, 'users/register.html', {'form': form})
            form.save()
            first_name=form.cleaned_data.get('first_name')
            messages.success(request,f'{first_name}! Now you can Login')
            return redirect('index')
    else:
        form = SignUpForm
        return render(request, 'users/register.html', {'form': form})





    
    
    
    
    
    
    
    
    
    
    
                 


     
    
    


