from django.shortcuts import render,redirect
from DOCTOR.decorates import auth_login
from ADMIN.models import login_det, patient_det

# Create your views here.
@auth_login
def patientdash(request):
     return render(request,'patdashboard.html')
@auth_login
def patientview1(request):
     patient=patient_det.objects.get(p_username=request.session['user_name'])
     msg=''
     if request.method == 'POST':
        if 'save' in request.POST:
            p_name = request.POST['pname']
            p_mob = request.POST['pnumber']
            p_email = request.POST['pemail']
            p_address = request.POST['paddress']
            p_district = request.POST['pdis']
            p_dob = request.POST['pdob']
            p_age = request.POST['page']
            p_gender = request.POST['pgender']
            patient_det.objects.filter(id=patient.id).update(p_name=p_name, p_mob=p_mob, p_email=p_email,
                            p_address=p_address, p_district=p_district, p_dob=p_dob, p_age=p_age, p_gender=p_gender)
            return redirect('/pat/patview')
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
                              patient_det.objects.filter(id=patient.id).update(p_password=confirm_pass)
                       else:
                              msg='Password doesnt match'
                  else:
                         msg='current password is invalid'

     return render(request,'patview.html',{'details':patient,'err':msg})

def patientapp(request):
     return render(request,'patfixapp.html')

def patientapplist(request):
     return render(request,'patapplist.html')

def patientlabr1(request):
     return render(request,'patlabreorts.html')

def patientlabdet(request):
     return render(request,'patlabdetail.html')

def patientpresl(request):
     return render(request,'patpreslist.html')

def patientpresdet(request):
     return render(request,'patpresdetail.html')

def patientbloodreq(request):
     return render(request,'patbldreq.html')
     
def patientbloodreqv(request):
     return render(request,'patbldreqview.html')
def plogout(request):
    del request.session['user_name']
    request.session.flush()
    return redirect('log1')