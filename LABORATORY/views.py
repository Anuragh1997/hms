from django.shortcuts import render

# Create your views here.
def Ldash(request):
     return render(request,'labdashboard.html')
def Lview(request):
     return render(request,'viewlab1.html')
def Lviewp(request):
     return render(request,'viewlabpat.html')
def Lviewpa(request):
     return render(request,'viewlabpatient.html')
def Lviewre(request):
     return render(request,'viewlabreports.html')
def Lviewrede(request):
     return render(request,'viewlabreportsdetail.html')
def Lviewrept(request):
     return render(request,'viewlabreportold.html')
def Lviewreold(request):
     return render(request,'viewlabreportoldview.html')