from django.urls import path
from . import views

urlpatterns = [
    
    path('docdashboard',views.Ddash,name="addashdoc"),
    path('docview1',views.Dview,name="docv"),
    path('viewapp',views.Dviewapp,name="docvapp"),
    path('viewappdet',views.Dviewappdet,name="docvappdet"),
    path('viewoldlab',views.Dviewlab,name="docpalab"),
    path('viewoldlabdet',views.Dviewlabdet,name="docpapdet"),
    path('viewoldpres',views.Dviewpres,name="docpapres"),
    path('viewoldpresdet',views.Dviewpresdet,name="docpapresdet"),
    path('viewpat',views.Dviewpat,name="docpat"),
    path('viewpres',views.Dviewpres1,name="docpres"),
    path('viewpresdet',views.Dviewpresdet1,name="docpresdet1")
    
    
    
]