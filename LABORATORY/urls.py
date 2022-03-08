from django.urls import path
from . import views

urlpatterns = [
    
    path('labdashboard',views.labdash,name="addashlab"),
    path('labview',views.labview,name="labview1"),
    path('labviewpat',views.labviewpatient,name="lbvwpt"),
    path('labviewpatient',views.labviewpat,name="lbviwpt"),
    path('labviewreport',views.labviewreport,name="lbviwrp"),
    path('labviewreportdetail',views.labviewrede,name="lbviwrpde"),
    path('labviewrepat',views.labviewrept,name="lbviwrpt"),
    path('labviewold',views.labviewreold,name="lbviwrold")
    
    
]