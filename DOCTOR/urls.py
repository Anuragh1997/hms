from django.urls import path
from . import views

urlpatterns = [
    
    path('docdashboard',views.doctordash,name="addashdoc"),
    path('docview1',views.doctorview,name="docv"),
    path('viewapp',views.docviewapp,name="docvapp"),
    path('viewappdet',views.dovviewappdet,name="docvappdet"),
    path('viewoldlab',views.dviewlab,name="docpalab"),
    path('viewoldlabdet',views.dviewlabdet,name="docpapdet"),
    path('viewoldpres',views.dviewpres,name="docpapres"),
    path('viewoldpresdet',views.dviewpresdet,name="docpapresdet"),
    path('viewpat',views.dviewpatient,name="docpat"),
    path('viewpres',views.dviewprescription1,name="docpres"),
    path('viewpresdet',views.dviewpresdetail1,name="docpresdet1"),
    path('log_out',views.logout,name="out")
    
    
    
]