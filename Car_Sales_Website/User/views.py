from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from .forms import RegisterForm,UserDetailChange
from django.urls import reverse_lazy
from django.contrib import messages
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
    return render(request,'register.html',{'form':form,'type':'Register'})

class Login(LoginView):
    template_name='register.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['type']='Login'
        return context
    def get_success_url(self):
        return reverse_lazy("Profile")
    def form_invalid(self, form):
        messages.warning(self.request,"Invalid Credentials")
        return super().form_invalid(form)
    def form_valid(self, form):
        messages.success(self.request,"Logged In Successfully")
        return super().form_valid(form)



            