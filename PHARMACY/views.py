from django.shortcuts import render

# Create your views here.
def Pdash(request):
     return render(request,'phadashboard.html')
def Pview123(request):
     return render(request,'phaview.html')
def Patviewph(request):
     return render(request,'phaviewpatlist.html')
def Patviewphd(request):
     return render(request,'phaviewpatdet.html')
def Phapres(request):
     return render(request,'phaviewppres.html')
def Phapresdet(request):
     return render(request,'phaviewppresdet.html')
def Phaprespat(request):
     return render(request,'phaviewpprespat.html')