from django.shortcuts import render,redirect
from DOCTOR.decorates import auth_login

# Create your views here.
@auth_login
def blooddash(request):
     return render(request,'blddashboard.html')

def bldview(request):
     return render(request,'bloodview.html')

def addblddonor(request):
     return render(request,'blooddonor.html')

def bdonorlist(request):
     return render(request,'blooddonorlist.html')

def bdonorview(request):
     return render(request,'blooddonorview.html')

def bldreq(request):
     return render(request,'bloodrequest1.html')

def breqview(request):
     return render(request,'bloodrequestview1.html')

def bldreqlist(request):
     return render(request,'bloodreclist.html')

def bldelivered(request):
     return render(request,'blooddellist.html')
def blogout(request):
    del request.session['user_id']
    request.session.flush()
    return redirect('log1')
