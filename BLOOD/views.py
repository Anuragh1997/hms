from django.shortcuts import render

# Create your views here.
def Bdash(request):
     return render(request,'blddashboard.html')
def Bview(request):
     return render(request,'bloodview.html')
def Bdonor(request):
     return render(request,'blooddonor.html')
def Bdlist(request):
     return render(request,'blooddonorlist.html')
def Bdview(request):
     return render(request,'blooddonorview.html')
def Breq(request):
     return render(request,'bloodrequest1.html')
def Breqview(request):
     return render(request,'bloodrequestview1.html')
def Brecli(request):
     return render(request,'bloodreclist.html')
def Bdelli(request):
     return render(request,'blooddellist.html')
