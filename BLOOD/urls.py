from django.urls import path
from . import views

urlpatterns = [
    
    path('blddashboard',views.Bdash,name="addashbld"),
    path('bldbanlview',views.Bview,name="bldview"),
    path('adddonor',views.Bdonor,name="blddonor"),
    path('donorlist',views.Bdlist,name="bldlist"),
    path('donorview',views.Bdview,name="blddv"),
    path('bloodrequest',views.Breq,name="bldreq"),
    path('bloodrequestview',views.Breqview,name="bldreqvi"),
    path('bloodreclist',views.Brecli,name="bldrec"),
    path('blooddellist',views.Bdelli,name="blddel")
   
    
]