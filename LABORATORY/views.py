from django.shortcuts import render

# Create your views here.
def labdash(request):
     return render(request,'labdashboard.html')

def labview(request):
     return render(request,'viewlab1.html')

def labviewpatient(request):
     return render(request,'viewlabpat.html')

def labviewpat(request):
     return render(request,'viewlabpatient.html')

def labviewreport(request):
     return render(request,'viewlabreports.html')

def labviewrede(request):
     return render(request,'viewlabreportsdetail.html')

def labviewrept(request):
     return render(request,'viewlabreportold.html')
     
def labviewreold(request):
     return render(request,'viewlabreportoldview.html')