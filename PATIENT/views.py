from django.shortcuts import render

# Create your views here.
def patientdash(request):
     return render(request,'patdashboard.html')

def patientview1(request):
     return render(request,'patview.html')

def patientapp(request):
     return render(request,'patfixapp.html')

def patientapplist(request):
     return render(request,'patapplist.html')

def patientlabr1(request):
     return render(request,'patlabreorts.html')

def patientlabdet(request):
     return render(request,'patlabdetail.html')

def patientpresl(request):
     return render(request,'patpreslist.html')

def patientpresdet(request):
     return render(request,'patpresdetail.html')

def patientbloodreq(request):
     return render(request,'patbldreq.html')
     
def patientbloodreqv(request):
     return render(request,'patbldreqview.html')