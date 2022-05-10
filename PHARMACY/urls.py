from django.urls import path
from . import views

urlpatterns = [
    
    path('phadashboard',views.pharmacydash,name="addashpha"),
    path('phaview',views.pharmacyview123,name="viewpha"),
    path('phapatlist',views.viewpatient,name="viewphapt"),
    path('phapatview/<int:id>',views.viewpatientdet,name="viewphaptd"),
    path('phapreslist',views.preslist,name="viewpres"),
    path('phapreslistdet/<int:id>',views.presdetailview,name="viewpresdet"),
    path('phaprespat/<int:id>',views.viewprespatient,name="viewprepat"),
    path('log_out',views.phlogout,name="phout")
    
    
    
]