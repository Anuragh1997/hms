from django.urls import path
from . import views

urlpatterns = [
    
    path('phadashboard',views.Pdash,name="addashpha"),
    path('phaview',views.Pview123,name="viewpha"),
    path('phapatlist',views.Patviewph,name="viewphapt"),
    path('phapatview',views.Patviewphd,name="viewphaptd"),
    path('phapreslist',views.Phapres,name="viewpres"),
    path('phapreslistdet',views.Phapresdet,name="viewpresdet"),
    path('phaprespat',views.Phaprespat,name="viewprepat")
    
    
    
]