from django.urls import path
from . import views

urlpatterns = [
    
    path('patdashboard',views.patientdash,name="addashpat"),
    path('patview',views.patientview1,name="pview"),
    path('patfixappoinment',views.patientapp,name="pfapp"),
    path('patlistapp',views.patientapplist,name="pfapplist"),
    path('patlabrep',views.patientlabr1,name="plabrep"),
    path('patlabdet',views.patientlabdet,name="prepd"),
    path('patpreslist',views.patientpresl,name="preli"),
    path('patpresview',views.patientpresdet,name="predet"),
    path('patbloodreq',views.patientbloodreq,name="pblreq"),
    path('patbloodreqview',views.patientbloodreqv,name="pblreqv"),
    path('log_out',views.plogout,name="pout")
    
    
]