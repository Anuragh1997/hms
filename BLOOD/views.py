from tokenize import group
from django.shortcuts import render,redirect
from DOCTOR.decorates import auth_login
from ADMIN.models import login_det, bloodbank_det
from .models import donor_det,bldrec_det
from datetime import datetime

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
@auth_login
def addblddonor(request):
     now = datetime.now()
     dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
     if request.method == 'POST':
        d_name = request.POST['bname']
        d_mob = request.POST['bnumber']
        d_group = request.POST['bgroup']
        d_address = request.POST['baddress']
        d_district = request.POST['bdis']
        d_dob = request.POST['bdob']
        d_age = request.POST['bage']
        d_gender = request.POST['bgender']
        donor = donor_det(do_name=d_name, do_mob=d_mob, do_group=d_group,
                            do_address=d_address, do_district=d_district, do_dob=d_dob, do_age=d_age, do_gender=d_gender,do_datetime=dt_string)
        
        donor.save()
       
     return render(request,'blooddonor.html')
@auth_login
def bdonorlist(request):
     donorlist=donor_det.objects.all()
     return render(request,'blooddonorlist.html',{'list':donorlist,})
@auth_login
def bdonorview(request,id):
     now = datetime.now()
     dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
     donor=donor_det.objects.get(id=id)
     if request.method == 'POST':
          if 'del' in request.POST:
               donor.delete()              
               return redirect('bldlist')
          if 'save' in request.POST:
               d_name = request.POST['bname']
               d_mob = request.POST['bnumber']
               d_group = request.POST['bgroup']
               d_address = request.POST['baddress']
               d_district = request.POST['bdis']
               d_dob = request.POST['bdob']
               d_age = request.POST['bage']
               d_gender = request.POST['bgender']
               donor_det.objects.filter(id=donor.id).update(do_name=d_name, do_mob=d_mob, do_group=d_group,
                            do_address=d_address, do_district=d_district, do_dob=d_dob, do_age=d_age, do_gender=d_gender)
               return redirect('/bld/donorview/%d'%id)
          if 'add' in request.POST:
               bd_date = request.POST['badd']
               group=donor.do_group
               received = bldrec_det(do_id_id=id, db_group=group,
                            db_date=bd_date,db_datetime=dt_string)
              
               received.save()
               return redirect('/bld/donorview/%d'%id)

     return render(request,'blooddonorview.html',{'details':donor})

def bldreq(request):
     return render(request,'bloodrequest1.html')

def breqview(request):
     return render(request,'bloodrequestview1.html')
@auth_login
def bldreclist(request):
      reclist=bldrec_det.objects.all()
      
      if request.method == 'POST':
            delid = request.POST['did']
            list=bldrec_det.objects.get(id=delid)
            list.delete()       
            return redirect('bldrec')

      return render(request,'bloodreclist.html',{'list':reclist,})

def bldelivered(request):
     return render(request,'blooddellist.html')
def blogout(request):
    del request.session['user_name']
    request.session.flush()
    return redirect('log1')
