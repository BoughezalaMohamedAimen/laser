from django.urls import path,include,re_path
from django.views.decorators.csrf import csrf_exempt
from .views import *
urlpatterns = [
    path('',HomeCaisse.as_view(),name='home_caisse'),
    path('update/<int:id>',UpdateCaisse.as_view(),name='update_caisse'),
    path('historique/libre/<int:id>',GetSeanceLibre,name='historique_seance_libre_page_num'),
]
