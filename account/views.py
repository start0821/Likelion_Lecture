from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = User.objects.create(username=username)
            user.set_password(password)
            user.save()
            return redirect('account:login')
        else:
            return render(request,'account/register.html',{'form':form})
    else:
        form = SignUpForm()
    return render(request,'account/register.html',{'form':form})

def login(request):
    return render(request, 'account/login.html', {'form':form})

def profile(request):
    return render(request, 'account/profile.html', {})

def index(request):
    return render(request, 'base.html')