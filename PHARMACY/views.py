from django.shortcuts import render,redirect
from DOCTOR.decorates import auth_login
from ADMIN.models import login_det, pharmacy_det,patient_det

# Create your views here.
@auth_login
def pharmacydash(request):
     return render(request,'phadashboard.html')
@auth_login
def pharmacyview123(request):
     pharmacy=pharmacy_det.objects.get(ph_username=request.session['user_name'])
     msg=''
     if request.method == 'POST':
        if 'save' in request.POST:
             ph_name = request.POST['phname']
             ph_mob = request.POST['phnumber']
             ph_details = request.POST['phdet']
             pharmacy_det.objects.filter(id=pharmacy.id).update(ph_name=ph_name, ph_num=ph_mob, ph_details=ph_details)
             return redirect('/pha/phaview')
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
                              pharmacy_det.objects.filter(id=pharmacy.id).update(ph_password=confirm_pass)
                       else:
                              msg='Password doesnt match'
                  else:
                         msg='current password is invalid'
     return render(request,'phaview.html',{'details':pharmacy,'err':msg})
@auth_login
def viewpatient(request):
     patientlist=patient_det.objects.all()
     return render(request,'phaviewpatlist.html',{'list':patientlist,})
@auth_login
def viewpatientdet(request,id):
     patient=patient_det.objects.get(id=id)
     return render(request,'phaviewpatdet.html',{'details':patient})

def preslist(request):
     return render(request,'phaviewppres.html')

def presdetailview(request):
     return render(request,'phaviewppresdet.html')
     
def viewprespatient(request):
     return render(request,'phaviewpprespat.html')
def phlogout(request):
    del request.session['user_name']
    request.session.flush()
    return redirect('log1')