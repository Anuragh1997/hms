from django.shortcuts import render,redirect
from DOCTOR.decorates import auth_login
from ADMIN.models import login_det, lab_det,patient_det
from .models import report_det
from datetime import datetime


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
@auth_login
def labviewpatient(request):
     patientlist=patient_det.objects.all()
     return render(request,'viewlabpat.html',{'list':patientlist,})
@auth_login
def labviewpat(request,id):
     now = datetime.now()
     dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
     patient=patient_det.objects.get(id=id)
     patid=patient.id
     if request.method == 'POST':
          r_name = request.POST['rname']
          r_des = request.POST['rdet']
          r_path = request.FILES['rfile']
          r_date = request.POST['rdate']
          reports = report_det(r_name=r_name, r_details=r_des, r_path=r_path,r_date=r_date,p_id_id=patid,r_addedby=request.session['user_name'],r_datetime=dt_string)
          reports.save()      
     return render(request,'viewlabpatient.html',{'details':patient})
@auth_login
def labviewreport(request):
     reportlist=report_det.objects.filter(r_addedby=request.session['user_name'])
     return render(request,'viewlabreports.html',{'list':reportlist,})
@auth_login
def labviewrede(request,id):
     report=report_det.objects.get(id=id)
     return render(request,'viewlabreportsdetail.html',{'details':report})

def labviewrept(request,id):
     report=report_det.objects.filter(p_id=id,r_addedby=request.session['user_name'])
     return render(request,'viewlabreportold.html',{'list':report})
     
def labviewreold(request):
     return render(request,'viewlabreportoldview.html')
def llogout(request):
    del request.session['user_name']
    request.session.flush()
    return redirect('log1')