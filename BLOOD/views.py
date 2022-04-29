from django.shortcuts import render,redirect
from DOCTOR.decorates import auth_login
from ADMIN.models import login_det, bloodbank_det

# Create your views here.
@auth_login
def blooddash(request):
     return render(request,'blddashboard.html')
@auth_login
def bldview(request):
     blood=bloodbank_det.objects.get(b_username=request.session['user_name'])
     msg=''
     if request.method == 'POST':
          if 'save' in request.POST:
               b_name = request.POST['blname']
               b_mob = request.POST['blnumber']
               b_details = request.POST['bldet']
               bloodbank_det.objects.filter(id=blood.id).update(b_name=b_name, b_num=b_mob, b_details=b_details)
               return redirect('/bld/bldbanlview')
          if 'savepass' in request.POST:
               details=login_det.objects.get(username=request.session['user_name'])
               password=details.password
               if request.method=="POST":
                    current_pass=request.POST['current_pass']
                    password1=request.POST['new_pass']
                    confirm_pass=request.POST['confirm_pass']
                    if current_pass==password:
                         if confirm_pass==password1:
                                   login_det.objects.filter(id=details.id).update(password=confirm_pass)
                                   bloodbank_det.objects.filter(id=blood.id).update(b_password=confirm_pass)
                         else:
                                   msg='Password doesnt match'
                    else:
                              msg='current password is invalid'
     return render(request,'bloodview.html',{'details':blood,'err':msg})

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
    del request.session['user_name']
    request.session.flush()
    return redirect('log1')
