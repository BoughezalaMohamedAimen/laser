from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .forms import *
from django.core.paginator import Paginator
from .models import *
from clients.models import SeanceHistorique
# Create your views here.
class HomeCaisse(TemplateView):
    def get(self,request):
        caisses_list=Caisse.objects.all().order_by('-date')
        paginator = Paginator(caisses_list, 30) # Show 25 clients per page
        page = request.GET.get('page')
        caisses = paginator.get_page(page)
        return render(request,'caisse/home.html',{'caisses':caisses})
#
#     def post(self,request):
#         form=CaisseForm(request.POST,prefix='add')
#         form_update=UpdateCaisseForm()
#         caisses=Caisse.objects.all()
#         if form.is_valid():
#             form.save()
#             form=CaisseForm()
#         return render(request,'caisses/home.html',{'form':form,'caisses':caisses,'form_update':form_update})
#
#
class UpdateCaisse(TemplateView):
    def get(self,request,id):
        caisse=Caisse.objects.get(id=id)
        form_update=UpdateCaisseForm(instance=caisse)
        return render(request,'caisse/update_caisse.html',{'caisse':caisse,'form_update':form_update})

    def post(self,request,id):
        form_update=UpdateCaisseForm(request.POST,prefix='update',instance=Caisse.objects.get(id=id))
        if form_update.is_valid():
            form_update.save()
        return redirect('home_caisse')


def GetSeanceLibre(request,id):
    caisse=Caisse.objects.get(id=id)
    print(caisse.date)
    historique_list=SeanceHistorique.objects.filter(client=None,date_heure__date=caisse.date).order_by('-date_heure')
    paginator = Paginator(historique_list, 10) # Show 25 clients per page
    page = request.GET.get('page')
    historiques = paginator.get_page(page)
    return render(request,'caisse/historique_seance-libre.html',{'historiques':historiques})
