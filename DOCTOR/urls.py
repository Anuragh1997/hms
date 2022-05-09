from django.urls import path
from . import views

urlpatterns = [
    
    path('docdashboard',views.doctordash,name="addashdoc"),
    path('docview1',views.doctorview,name="docv"),
    path('viewapp',views.docviewapp,name="docvapp"),
    path('viewappdet',views.dovviewappdet,name="docvappdet"),
    path('viewoldlab/<int:id>',views.dviewlab,name="docpalab"),
    path('viewoldlabdet/<int:id>',views.dviewlabdet,name="docpapdet"),
    path('viewoldpres/<int:id>',views.dviewpres,name="docpapres"),
    path('viewoldpresdet/<int:id>',views.dviewpresdet,name="docpapresdet"),
    path('viewpat',views.dviewpatient,name="docpat"),
    path('viewpatdet/<int:id>',views.dovviewpatdet,name="patdetail"),
    path('viewpres',views.dviewprescription1,name="docpres"),
    path('viewpresdet/<int:id>',views.dviewpresdetail1,name="docpresdet1"),
    path('log_out',views.logout,name="out")
    
    
    
]