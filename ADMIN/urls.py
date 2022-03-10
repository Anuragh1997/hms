from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login),
    path('dashboard',views.dashboard,name="addash"),
    path('adddoc',views.adddoctor,name="addoc"),
    path('doclist',views.doctorlist,name="doctlist"),
    path('appoinment',views.addappoinment,name="addapp"),
    path('appoinmentlist',views.appoinmentlist1,name="applist"),
    path('addpatient',views.addpatient,name="addpat"),
    path('pattientlist',views.patlist,name="patlist"),
    path('addlabs',views.lab,name="addlab"),
    path('lablist',views.lablist,name="lalist"), 
    path('report',views.labreport,name="reprt"),
    path('addphar',views.pharmacy,name="addpha"),
    path('phalist',views.phalist,name="phlist"),
    path('pres',views.prescription,name="presli"),
    path('addblood',views.blood,name="addbld"),
    path('bloodlist',views.bldlist,name="bllist"),
    path('bloodreq',views.bldreq,name="blreq"),
    path('bloodreqview',views.viewreq,name="blreqv"),
    path('viewdoctor',views.viewdoc,name="viewdr"),
    path('viewdoctorapp',views.viewdocapp,name="viewapp"),
    path('viewpatient',views.viewpatient,name="viewpat"),
    path('viewlabo',views.viewlab,name="viewlab"),
    path('viewreport',views.viewlabrep,name="viewlabreport"),
    path('viewphar1',views.viewpharmacy1,name="viewpha1"),
    path('viewpharre',views.viewphre,name="viewpresdetailed"),
    path('viewblood',views.viewbld,name="viewbld")
    
]