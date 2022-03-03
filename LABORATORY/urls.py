from django.urls import path
from . import views

urlpatterns = [
    
    path('labdashboard',views.Ldash,name="addashlab"),
    path('labview',views.Lview,name="labview1"),
    path('labviewpat',views.Lviewp,name="lbvwpt"),
    path('labviewpatient',views.Lviewpa,name="lbviwpt"),
    path('labviewreport',views.Lviewre,name="lbviwrp"),
    path('labviewreportdetail',views.Lviewrede,name="lbviwrpde"),
    path('labviewrepat',views.Lviewrept,name="lbviwrpt"),
    path('labviewold',views.Lviewreold,name="lbviwrold")
    
    
]