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
    path('pattientlist',views.Patlist,name="patlist"),
    path('addlabs',views.Lab,name="addlab"),
    path('lablist',views.Lablist,name="lalist"), 
    path('report',views.Report,name="reprt"),
    path('addphar',views.Pha,name="addpha"),
    path('phalist',views.Phalist,name="phlist"),
    path('pres',views.Pres,name="presli"),
    path('addblood',views.Blood,name="addbld"),
    path('bloodlist',views.Bldlist,name="bllist"),
    path('bloodreq',views.Bldreq,name="blreq"),
    path('bloodreqview',views.Viewreq,name="blreqv"),
    path('viewdoctor',views.Viewdoc,name="viewdr"),
    path('viewdoctorapp',views.Viewdocapp,name="viewapp"),
    path('viewpatient',views.Viewpati,name="viewpat")
]