from django.urls import path
from . import views

urlpatterns = [
    
    path('labdashboard',views.labdash,name="addashlab"),
    path('labview',views.labview,name="labview1"),
    path('labviewpat',views.labviewpatient,name="lbvwpt"),
    path('labviewpatient/<int:id>',views.labviewpat,name="lbviwpt"),
    path('labviewreport',views.labviewreport,name="lbviwrp"),
    path('labviewreportdetail/<int:id>',views.labviewrede,name="lbviwrpde"),
    path('labviewrepat/<int:id>',views.labviewrept,name="lbviwrpt"),
    path('labviewold/<int:id>',views.labviewreold,name="lbviwrold"),
    path('log_out',views.llogout,name="lgout")
    
    
]