from django.urls import path
from . import views

urlpatterns = [
    
    path('blddashboard',views.blooddash,name="addashbld"),
    path('bldbanlview',views.bldview,name="bldview"),
    path('adddonor',views.addblddonor,name="blddonor"),
    path('donorlist',views.bdonorlist,name="bldlist"),
    path('donorview',views.bdonorview,name="blddv"),
    path('bloodrequest',views.bldreq,name="bldreq"),
    path('bloodrequestview',views.breqview,name="bldreqvi"),
    path('bloodreclist',views.bldreqlist,name="bldrec"),
    path('blooddellist',views.bldelivered,name="blddel")
   
    
]