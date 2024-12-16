from django.shortcuts import redirect
from django.views.generic import DetailView
from .models import CarModel,PurchaseModel
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
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
        context['car']=car
        return context
@login_required  
def BuyCar(request,id):
    car=CarModel.objects.get(pk=id)
    purchase_obj=PurchaseModel.objects.create(user=request.user,car=car)
    purchase_obj.save()
    car.quantity=car.quantity-1
    car.save()
    return redirect("CarDetail",id=car.id)

