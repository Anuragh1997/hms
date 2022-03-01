from django.shortcuts import render

# Create your views here.
def Log(request):
     return render(request,'adminlogin.html')
def Dash(request):
     return render(request,'admindashboard.html')
def Doc(request):
     return render(request,'adddoctor.html')
def Doclist(request):
     return render(request,'doctorlist.html')
def Appoinment(request):
     return render(request,'addappoinment.html')
def Appoinmentlist1(request):
     return render(request,'appoinmentlist.html')
def Pat(request):
     return render(request,'addpatient.html')
def Patlist(request):
     return render(request,'patientlist.html')
def Lab(request):
     return render(request,'addlab.html')
def Lablist(request):
     return render(request,'lablist.html')
def Report(request):
     return render(request,'labreports.html')
def Pha(request):
     return render(request,'addpha.html')
def Phalist(request):
     return render(request,'phalist.html')
def Pres(request):
     return render(request,'preslist.html')
def Blood(request):
     return render(request,'addblood.html')
def Bldlist(request):
     return render(request,'bloodlist.html')
def Bldreq(request):
     return render(request,'bloodrequest.html')
def Viewreq(request):
     return render(request,'bloodrequestview.html')
def Viewdoc(request):
     return render(request,'viewdoctor.html')
def Viewdocapp(request):
     return render(request,'viewappoinment.html')
def Viewpati(request):
     return render(request,'viewpatient.html')

