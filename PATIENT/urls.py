from django.urls import path
from . import views

urlpatterns = [
    
    path('patdashboard',views.Pdash,name="addashpat"),
    path('patview',views.Pview1,name="pview"),
    path('patfixappoinment',views.Papp,name="pfapp"),
    path('patlistapp',views.Papplist,name="pfapplist"),
    path('patlabrep',views.Plabr1,name="plabrep"),
    path('patlabdet',views.Plabd,name="prepd"),
    path('patpreslist',views.Ppresl,name="preli"),
    path('patpresview',views.Ppresdet,name="predet"),
    path('patbloodreq',views.Pbloodreq,name="pblreq"),
    path('patbloodreqview',views.Pbloodreqv,name="pblreqv")
    
    
]