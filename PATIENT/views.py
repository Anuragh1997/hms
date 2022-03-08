from django.shortcuts import render

# Create your views here.
def Pdash(request):
     return render(request,'patdashboard.html')
def Pview1(request):
     return render(request,'patview.html')
def Papp(request):
     return render(request,'patfixapp.html')
def Papplist(request):
     return render(request,'patapplist.html')
def Plabr1(request):
     return render(request,'patlabreorts.html')
def Plabd(request):
     return render(request,'patlabdetail.html')
def Ppresl(request):
     return render(request,'patpreslist.html')
def Ppresdet(request):
     return render(request,'patpresdetail.html')
def Pbloodreq(request):
     return render(request,'patbldreq.html')
def Pbloodreqv(request):
     return render(request,'patbldreqview.html')