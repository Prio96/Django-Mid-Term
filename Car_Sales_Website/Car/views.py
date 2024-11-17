from django.shortcuts import render,redirect
from django.views.generic import DetailView
from .models import CarModel
from .forms import CommentForm
# Create your views here.

class CarDetail(DetailView):
    model=CarModel
    pk_url_kwarg='id'
    template_name='car_detail.html'
    
    def post(self, request, *args, **kwargs):
        car=self.get_object()
        comment_form=CommentForm(data=self.request.POST)
        if comment_form.is_valid():
            comment=comment_form.save(commit=False)
            comment.car=car
            comment_form.save()
            return self.get(request,*args,**kwargs)
        
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        car=self.get_object()
        comments=car.comments.all()
        comment_form=CommentForm()
        context['comments']=comments
        context['comment_form']=comment_form
        return context
    
def BuyCar(request):
    car=CarModel.objects.get(pk=id)
    car.quantity=car.quantity-1
    return redirect("CarDetail")

