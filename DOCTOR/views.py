from django.shortcuts import render,redirect
from DOCTOR.decorates import auth_login
from ADMIN.models import login_det, doctor_det,patient_det
from .models import prescription_det
from LABORATORY.models import report_det
from datetime import datetime

# Create your views here.
@auth_login
def doctordash(request):
     return render(request,'docdashboard.html')
@auth_login
def doctorview(request):
     doctor=doctor_det.objects.get(d_username=request.session['user_name'])
     msg=''
     if request.method == 'POST':
        if 'save' in request.POST:
            d_name = request.POST['drname']
            d_mob = request.POST['drnumber']
            d_email = request.POST['dremail']
            d_address = request.POST['draddress']
            d_district = request.POST['drdistrict']
            d_dob = request.POST['drdob']
            d_dep = request.POST['drdep']
            d_gender = request.POST['drgender']
            doctor_det.objects.filter(id=doctor.id).update(d_name=d_name, d_mob=d_mob, d_email=d_email,
                            d_address=d_address, d_district=d_district, d_dob=d_dob, d_department=d_dep, d_gender=d_gender)
            return redirect('/doc/docview1')
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
                              doctor_det.objects.filter(id=doctor.id).update(d_password=confirm_pass)
                       else:
                              msg='Password doesnt match'
                  else:
                         msg='current password is invalid'
     return render(request,'docview.html',{'details':doctor,'err':msg})
@auth_login
def docviewapp(request):
     return render(request,'docviewapp.html')
@auth_login
def dovviewappdet(request):
     return render(request,'docviewappdet.html')
@auth_login
def dviewlab(request,id):
     reports=report_det.objects.filter(p_id_id=id)

     return render(request,'doclabreports.html',{'list':reports,})
@auth_login
def dviewpres(request,id):
     pres=prescription_det.objects.filter(p_id_id=id)
     return render(request,'docviewpres.html',{'list':pres,})
@auth_login
def dviewlabdet(request,id):
     report=report_det.objects.get(id=id)
     return render(request,'docviewlabdetail.html',{'details':report})
@auth_login
def dviewpresdet(request,id):
     pres=prescription_det.objects.get(id=id)
     return render(request,'docviewpresdetail.html',{'details':pres})
@auth_login
def dviewpatient(request):
     patientlist=patient_det.objects.all()
     return render(request,'docviewpat.html',{'list':patientlist,})
@auth_login
def dovviewpatdet(request,id):
     patient=patient_det.objects.get(id=id)
     patientid=patient.id
     details=doctor_det.objects.get(d_username=request.session['user_name'])
     doc=details.id
     now = datetime.now()
     dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
     if request.method == 'POST':
          pr = request.POST['pres']
          prescription = prescription_det(p_id_id=patientid, d_id_id=doc, pres=pr,datetime=dt_string)
          prescription.save()  
          return redirect('/doc/viewpatdet/%d'%id) 
          
     return render(request,'docviewpatdet.html',{'details':patient,})
@auth_login
def dviewprescription1(request):
     details=doctor_det.objects.get(d_username=request.session['user_name'])
     doc=details.id
     pres=prescription_det.objects.filter(d_id_id=doc)
     return render(request,'docviewpres1.html',{'list':pres,})
@auth_login    
def dviewpresdetail1(request,id):
     pres=prescription_det.objects.get(id=id)
     if 'del' in request.POST:
          pres.delete()
          return redirect('docpres')
     if 'save' in request.POST:
          pr = request.POST['pres']
          prescription_det.objects.filter(id=id).update(pres=pr)
          return redirect('/doc/viewpresdet/%d'%id)
     return render(request,'docviewpresdet1.html',{'details':pres})
def logout(request):
    del request.session['user_name']
    request.session.flush()
    return redirect('log1')