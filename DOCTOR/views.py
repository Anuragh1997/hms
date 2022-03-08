from django.shortcuts import render

# Create your views here.
def doctordash(request):
     return render(request,'docdashboard.html')

def doctorview(request):
     return render(request,'docview.html')

def docviewapp(request):
     return render(request,'docviewapp.html')

def dovviewappdet(request):
     return render(request,'docviewappdet.html')

def dviewlab(request):
     return render(request,'doclabreports.html')

def dviewpres(request):
     return render(request,'docviewpres.html')

def dviewlabdet(request):
     return render(request,'docviewlabdetail.html')

def dviewpresdet(request):
     return render(request,'docviewpresdetail.html')

def dviewpatient(request):
     return render(request,'docviewpat.html')

def dviewprescription1(request):
     return render(request,'docviewpres1.html')
     
def dviewpresdetail1(request):
     return render(request,'docviewpresdet1.html')