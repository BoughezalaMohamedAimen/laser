from django.urls import path,include,re_path
from .views import *
urlpatterns = [
    path('',HomeForfait.as_view(),name='home_forfaits'),
    path('update/<int:id>',UpdateForfait.as_view(),name='update_forfaits'),
]
