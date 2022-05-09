from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login,name="log"),
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
    path('viewdoctor/<int:id>',views.viewdoc,name="viewdr"),
    path('viewdoctorapp',views.viewdocapp,name="viewapp"),
    path('viewpatient/<int:id>',views.viewpatient,name="viewpat"),
    path('viewlabo/<int:id>',views.viewlab,name="viewlab"),
    path('viewreport',views.viewlabrep,name="viewlabreport"),
    path('viewphar1/<int:id>',views.viewpharmacy1,name="viewpha1"),
    path('viewpharre',views.viewphre,name="viewpresdetailed"),
    path('viewblood/<int:id>',views.viewbld,name="viewbld"),
    path('logout',views.adminlogout,name="log_out"),
    path('checkuser',views.drcheck,name="check_dr"),
    path('test',views.hometest,name="testing")
    
]