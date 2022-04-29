from django.shortcuts import render,redirect
from DOCTOR.decorates import auth_login
from ADMIN.models import login_det, lab_det

# Create your views here.
@auth_login
def labdash(request):
     return render(request,'labdashboard.html')
@auth_login
def labview(request):
     lab=lab_det.objects.get(l_username=request.session['user_name'])
     msg=''
     if request.method == 'POST':
        if 'save' in request.POST:
             l_name = request.POST['lbname']
             l_mob = request.POST['lbnumber']
             l_details = request.POST['lbdet']
             lab_det.objects.filter(id=lab.id).update(l_name=l_name, l_num=l_mob, l_details=l_details)
             return redirect('/lab/labview')
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
                              lab_det.objects.filter(id=lab.id).update(l_password=confirm_pass)
                       else:
                              msg='Password doesnt match'
                  else:
                         msg='current password is invalid'
     return render(request,'viewlab1.html',{'details':lab,'err':msg})

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
def llogout(request):
    del request.session['user_name']
    request.session.flush()
    return redirect('log1')