from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .forms import *
# Create your views here.
class HomeForfait(TemplateView):
    def get(self,request):
        form=ForfaitForm()
        form_update=UpdateForfaitForm()
        forfaits=Forfait.objects.all()
        return render(request,'forfaits/home.html',{'form':form,'forfaits':forfaits,'form_update':form_update})

    def post(self,request):
        form=ForfaitForm(request.POST,prefix='add')
        form_update=UpdateForfaitForm()
        forfaits=Forfait.objects.all()
        if form.is_valid():
            form.save()
            form=ForfaitForm()
        return render(request,'forfaits/home.html',{'form':form,'forfaits':forfaits,'form_update':form_update})


class UpdateForfait(TemplateView):
    def post(self,request,id):
        form_update=UpdateForfaitForm(request.POST,prefix='update',instance=Forfait.objects.get(id=id))
        if form_update.is_valid():
            form_update.save()
        return redirect('home_forfaits')
