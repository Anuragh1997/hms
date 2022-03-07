from django.shortcuts import render

# Create your views here.
def Ddash(request):
     return render(request,'docdashboard.html')
def Dview(request):
     return render(request,'docview.html')
def Dviewapp(request):
     return render(request,'docviewapp.html')
def Dviewappdet(request):
     return render(request,'docviewappdet.html')
def Dviewlab(request):
     return render(request,'doclabreports.html')
def Dviewpres(request):
     return render(request,'docviewpres.html')
def Dviewlabdet(request):
     return render(request,'docviewlabdetail.html')
def Dviewpresdet(request):
     return render(request,'docviewpresdetail.html')
def Dviewpat(request):
     return render(request,'docviewpat.html')
def Dviewpres1(request):
     return render(request,'docviewpres1.html')
def Dviewpresdet1(request):
     return render(request,'docviewpresdet1.html')