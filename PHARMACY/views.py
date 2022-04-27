from django.shortcuts import render,redirect
from DOCTOR.decorates import auth_login

# Create your views here.
@auth_login
def pharmacydash(request):
     return render(request,'phadashboard.html')

def pharmacyview123(request):
     return render(request,'phaview.html')

def viewpatient(request):
     return render(request,'phaviewpatlist.html')

def viewpatientdet(request):
     return render(request,'phaviewpatdet.html')

def preslist(request):
     return render(request,'phaviewppres.html')

def presdetailview(request):
     return render(request,'phaviewppresdet.html')
     
def viewprespatient(request):
     return render(request,'phaviewpprespat.html')
def phlogout(request):
    del request.session['user_id']
    request.session.flush()
    return redirect('log1')