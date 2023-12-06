from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *  
from .forms import *
# Create your views here.


@login_required
def personasIndex(request):

    if request.user.is_superuser:
        return render(request, 'moduloUser/dashboard_admin.html')
    elif request.user.is_staff:
        return render(request, 'moduloUser/dashboard_user.html')
    else:
        return render(request, 'moduloUser/dashboard_user.html')
    

def signUp(request):
    usuario = Usuario
    form = SignUpForm
    if request.method == "post":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'registration/signUp.html', {'form':form})