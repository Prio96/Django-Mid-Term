from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from .forms import RegisterForm,UserDetailChange
# Create your views here.

def Register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect("HomePage")
    else:
        form=RegisterForm()
    return render(request,'register.html',{'form':form})
            