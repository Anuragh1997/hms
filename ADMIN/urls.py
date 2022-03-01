from django.urls import path
from . import views

urlpatterns = [
    path('login',views.Log),
    path('dashboard',views.Dash,name="addash"),
    path('adddoc',views.Doc,name="addoc"),
    path('doclist',views.Doclist,name="doctlist"),
    path('appoinment',views.Appoinment,name="addapp"),
    path('appoinmentlist',views.Appoinmentlist1,name="applist"),
    path('addpatient',views.Pat,name="addpat"),
    path('patlist',views.Patlist,name="patlist"),
    path('addlab',views.Lab,name="addlab"),
    path('lablist',views.Lablist,name="lalist"), 
    path('report',views.Report,name="reprt")    
]