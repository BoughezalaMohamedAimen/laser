from django.urls import path,include,re_path
from django.views.decorators.csrf import csrf_exempt
from .views import *
urlpatterns = [
    path('',HomeClient.as_view(),name='home_clients'),
    path('update/<int:id>',UpdateClient.as_view(),name='update_clients'),
    path('get/rfid',csrf_exempt(GetClient.as_view()),name='by_rfid_clients'),
    path('seance/<int:id>/<int:suplaimentaire>',MarquerSeance,name='marquer_seance_clients'),
    path('seance/anuller/<int:id>',AnullerSeance,name='suprimmer_seance_clients'),
    path('historique/presence/<int:id>',GetHistorique,name='historique_page_num'),
    path('historique/payement/<int:id>',GetHistoriquePayement,name='historique_payment_page_num'),
    path('abonement/<int:id>',UpdateClientAbonement.as_view(),name='update_abonnement'),
    path('abonement/delete/<int:id>',DeleteClientAbonement.as_view(),name='delete_abonnement'),
]
