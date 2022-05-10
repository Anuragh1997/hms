from email import message
from django.shortcuts import render, redirect
from .decorates import auth_login
from . models import login_det, doctor_det,patient_det,lab_det,pharmacy_det,bloodbank_det
from datetime import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse,HttpResponse
from LABORATORY.models import report_det
from DOCTOR.models import prescription_det
# Create your views here.


def login(request):
    msg = ''
    if request.method == 'POST':
        ausername = request.POST['username']
        apassword = request.POST['password']
        userexist = login_det.objects.filter(
            username=ausername, password=apassword, status='1').exists()
        if userexist:
            userdetail = login_det.objects.get(
                username=ausername, password=apassword, status='1')
            request.session['user_id'] = userdetail.id

            return redirect('addash')
        else:
            msg = 'invalid username or password'

    return render(request, 'adminlogin.html', {'err_msg': msg, })


@auth_login
def dashboard(request):
    return render(request, 'admindashboard.html')


@auth_login
def adddoctor(request):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    if request.method == 'POST':
        d_name = request.POST['drname']
        d_mob = request.POST['drnumber']
        d_email = request.POST['dremail']
        d_address = request.POST['draddress']
        d_district = request.POST['drdistrict']
        d_dob = request.POST['drdob']
        d_dep = request.POST['drdep']
        d_gender = request.POST['drgender']
        doctor = doctor_det(d_name=d_name, d_mob=d_mob, d_email=d_email,
                            d_address=d_address, d_district=d_district, d_dob=d_dob, d_department=d_dep, d_gender=d_gender, d_username=d_email,d_password=d_mob,d_datetime=dt_string)
        login = login_det(username=d_email, password=d_mob,
                          status='2', datetime=dt_string)
        doctor.save()
        login.save()

    return render(request, 'adddoctor.html')

@auth_login
def doctorlist(request):
     doctorlist=doctor_det.objects.all()
     
     return render(request, 'doctorlist.html',{'list':doctorlist,})


def addappoinment(request):
    doctor=doctor_det.objects.all()
    patient=patient_det.objects.all()
    return render(request, 'addappoinment.html',{'doc':doctor,'pat':patient})


def appoinmentlist1(request):
    return render(request, 'appoinmentlist.html')

@auth_login
def addpatient(request):
     now = datetime.now()
     dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
     if request.method == 'POST':
        p_name = request.POST['pname']
        p_mob = request.POST['pnumber']
        p_email = request.POST['pemail']
        p_address = request.POST['paddress']
        p_district = request.POST['pdistrict']
        p_dob = request.POST['pdob']
        p_age = request.POST['page']
        p_gender = request.POST['pgender']
        patient = patient_det(p_name=p_name, p_mob=p_mob, p_email=p_email,
                            p_address=p_address, p_district=p_district, p_dob=p_dob, p_age=p_age, p_gender=p_gender, p_username=p_email,p_password=p_mob,p_datetime=dt_string)
        login = login_det(username=p_email, password=p_mob,
                          status='3', datetime=dt_string)
        patient.save()
        login.save()
     return render(request, 'addpatient.html')

@auth_login
def patlist(request):
     patientlist=patient_det.objects.all()
     return render(request, 'patientlist.html',{'list':patientlist,})

@auth_login
def lab(request):
     now = datetime.now()
     dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
     if request.method == 'POST':
        l_name = request.POST['lbname']
        l_mob = request.POST['lbnumber']
        l_details = request.POST['lbdet']
        
        lab = lab_det(l_name=l_name, l_num=l_mob, l_details=l_details,l_username=l_name,l_password=l_mob,l_datetime=dt_string)
        login = login_det(username=l_name, password=l_mob,
                          status='4', datetime=dt_string)
        lab.save()
        login.save()
     return render(request, 'addlab.html')

@auth_login
def lablist(request):
     lablist=lab_det.objects.all()
     return render(request, 'lablist.html',{'list':lablist,})


def labreport(request):
    reportlist=report_det.objects.all()
    return render(request, 'labreports.html',{'list':reportlist,})

@auth_login
def pharmacy(request):
     now = datetime.now()
     dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
     if request.method == 'POST':
        ph_name = request.POST['phname']
        ph_mob = request.POST['phnumber']
        ph_details = request.POST['phdet']
        
        pharmacy = pharmacy_det(ph_name=ph_name, ph_num=ph_mob, ph_details=ph_details,ph_username=ph_name,ph_password=ph_mob,ph_datetime=dt_string)
        login = login_det(username=ph_name, password=ph_mob,
                          status='5', datetime=dt_string)
        pharmacy.save()
        login.save()
     return render(request, 'addpha.html')

@auth_login
def phalist(request):
     phalist=pharmacy_det.objects.all()
     return render(request, 'phalist.html',{'list':phalist,})


def prescription(request):
    pres=prescription_det.objects.all()
    return render(request, 'preslist.html',{'list':pres,})

@auth_login
def blood(request):
     now = datetime.now()
     dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
     if request.method == 'POST':
        b_name = request.POST['blname']
        b_mob = request.POST['blnumber']
        b_details = request.POST['bldet']
        
        blood = bloodbank_det(b_name=b_name, b_num=b_mob, b_details=b_details,b_username=b_name,b_password=b_mob,b_datetime=dt_string)
        login = login_det(username=b_name, password=b_mob,
                          status='6', datetime=dt_string)
        blood.save()
        login.save()
     return render(request, 'addblood.html')

@auth_login
def bldlist(request):
     bldlist=bloodbank_det.objects.all()
     return render(request, 'bloodlist.html',{'list':bldlist,})


def bldreq(request):
    return render(request, 'bloodrequest.html')


def viewreq(request):
    return render(request, 'bloodrequestview.html')

@auth_login
def viewdoc(request,id):
    doctor=doctor_det.objects.get(id=id)
    if request.method == 'POST':
        if 'del' in request.POST:
            login=login_det.objects.get(username=doctor.d_username)
            doctor.delete()
            login.delete()
            return redirect('doctlist')
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
            return redirect('/aadmin/viewdoctor/%d'%id)
    return render(request, 'viewdoctor.html',{'details':doctor})


def viewdocapp(request):
    return render(request, 'viewappoinment.html')

@auth_login
def viewpatient(request,id):
    patient=patient_det.objects.get(id=id)
    if request.method == 'POST':
        if 'del' in request.POST:
            login=login_det.objects.get(username=patient.p_username)
            patient.delete()
            login.delete()
            return redirect('patlist')
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
            return redirect('/aadmin/viewpatient/%d'%id)
    return render(request, 'viewpatient.html',{'details':patient})

@auth_login
def viewlab(request,id):
    lab=lab_det.objects.get(id=id)
    if request.method == 'POST':
        if 'del' in request.POST:
            login=login_det.objects.get(username=lab.l_username)
            lab.delete()
            login.delete()
            return redirect('lalist')
        if 'save' in request.POST:
            l_name = request.POST['lbname']
            l_mob = request.POST['lbnumber']
            l_details = request.POST['lbdet']
            lab_det.objects.filter(id=lab.id).update(l_name=l_name, l_num=l_mob, l_details=l_details)
            return redirect('/aadmin/viewlabo/%d'%id)
    return render(request, 'viewlab.html',{'details':lab})


def viewlabrep(request,id):
    report=report_det.objects.get(id=id)
    return render(request, 'viewlabreport.html',{'details':report})

@auth_login
def viewpharmacy1(request,id):
    pharmacy=pharmacy_det.objects.get(id=id)
    if request.method == 'POST':
        if 'del' in request.POST:
            login=login_det.objects.get(username=pharmacy.ph_username)
            pharmacy.delete()
            login.delete()
            return redirect('phlist')
        if 'save' in request.POST:
            ph_name = request.POST['phname']
            ph_mob = request.POST['phnumber']
            ph_details = request.POST['phdet']
            pharmacy_det.objects.filter(id=pharmacy.id).update(ph_name=ph_name, ph_num=ph_mob, ph_details=ph_details)
            return redirect('/aadmin/viewphar1/%d'%id)
    return render(request, 'viewpharmacy1.html',{'details':pharmacy})


def viewphre(request,id):
    pres=prescription_det.objects.get(id=id)
    return render(request, 'viewphreport.html',{'details':pres})

@auth_login
def viewbld(request,id):
    blood=bloodbank_det.objects.get(id=id)
    if request.method == 'POST':
        if 'del' in request.POST:
            login=login_det.objects.get(username=blood.b_username)
            blood.delete()
            login.delete()
            return redirect('bllist')
        if 'save' in request.POST:
            b_name = request.POST['blname']
            b_mob = request.POST['blnumber']
            b_details = request.POST['bldet']
            bloodbank_det.objects.filter(id=blood.id).update(b_name=b_name, b_num=b_mob, b_details=b_details)
            return redirect('/aadmin/viewblood/%d'%id)

    return render(request, 'viewblood.html',{'details':blood})


def adminlogout(request):
    del request.session['user_id']
    request.session.flush()
    return redirect('log')


def drcheck(request):
    dusername = request.POST['dremail']
    userexist = login_det.objects.filter(username=dusername).exists()

    return JsonResponse({'status': userexist, })

@api_view(['GET'])
def hometest(request):
    message="congratzzz"
    return Response(message)