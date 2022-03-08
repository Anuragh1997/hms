from django.urls import path
from . import views

urlpatterns = [
    
    path('phadashboard',views.pharmacydash,name="addashpha"),
    path('phaview',views.pharmacyview123,name="viewpha"),
    path('phapatlist',views.viewpatient,name="viewphapt"),
    path('phapatview',views.viewpatientdet,name="viewphaptd"),
    path('phapreslist',views.preslist,name="viewpres"),
    path('phapreslistdet',views.presdetailview,name="viewpresdet"),
    path('phaprespat',views.viewprespatient,name="viewprepat")
    
    
    
]