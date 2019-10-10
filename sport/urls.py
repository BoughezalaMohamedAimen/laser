from dateutil.relativedelta import relativedelta
"""sport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static

def Home(request):
    return redirect('home_clients')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home ,name='home'),
    re_path(r'^forfait/', include('forfaits.urls')),
    re_path(r'^client/', include('clients.urls')),
    re_path(r'^caisse/', include('caisse.urls')),
]+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header='Administration du Site'





#create new caisse every day
from caisse.models import Caisse
import datetime
try:
    caisse=Caisse.objects.get(date=datetime.date.today())
except ObjectDoesNotExist:
    Caisse().save()


##delete invalid seance
from clients.models import Client

try:
    clients=Client.objects.filter(date_fin__lte=datetime.date.today(),status='False',seance__gte=0)
    for client in clients:
        client.date_fin=datetime.date.today()
        client.seance=0
        client.status='True'  #if we have already change it automatically
        client.save()
except:
    pass


##backup database
from shutil import copyfile
copyfile('db.sqlite3', 'c:/backup/'+str(datetime.date.today())+'.sqlite3')
