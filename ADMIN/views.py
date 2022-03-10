from django.shortcuts import render

# Create your views here.
def login(request):
     return render(request,'adminlogin.html')

def dashboard(request):
     return render(request,'admindashboard.html')

def adddoctor(request):
     return render(request,'adddoctor.html')

def doctorlist(request):
     return render(request,'doctorlist.html')

def addappoinment(request):
     return render(request,'addappoinment.html')

def appoinmentlist1(request):
     return render(request,'appoinmentlist.html')

def addpatient(request):
     return render(request,'addpatient.html')

def patlist(request):
     return render(request,'patientlist.html')

def lab(request):
     return render(request,'addlab.html')

def lablist(request):
     return render(request,'lablist.html')

def labreport(request):
     return render(request,'labreports.html')

def pharmacy(request):
     return render(request,'addpha.html')

def phalist(request):
     return render(request,'phalist.html')

def prescription(request):
     return render(request,'preslist.html')

def blood(request):
     return render(request,'addblood.html')

def bldlist(request):
     return render(request,'bloodlist.html')

def bldreq(request):
     return render(request,'bloodrequest.html')

def viewreq(request):
     return render(request,'bloodrequestview.html')

def viewdoc(request):
     return render(request,'viewdoctor.html')

def viewdocapp(request):
     return render(request,'viewappoinment.html')

def viewpatient(request):
     return render(request,'viewpatient.html')

def viewlab(request):
     return render(request,'viewlab.html')

def viewlabrep(request):
     return render(request,'viewlabreport.html')

def viewpharmacy1(request):
     return render(request,'viewpharmacy1.html')

def viewphre(request):
     return render(request,'viewphreport.html')
     
def viewbld(request):
     return render(request,'viewblood.html')


