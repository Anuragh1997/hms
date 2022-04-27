from django.shortcuts import render,redirect
from ADMIN. models import login_det

# Create your views here.
def login(request):
    msg = ''
    if request.method == 'POST':
        ausername = request.POST['username']
        apassword = request.POST['pass']
        userexist = login_det.objects.filter(
            username=ausername, password=apassword).exists()
        if userexist:
            userdetail = login_det.objects.get(
                username=ausername, password=apassword)
            
            if userdetail.status == '2':
                request.session['user_id'] = userdetail.id
                return redirect('addashdoc')
            if userdetail.status == '3':
                request.session['user_id'] = userdetail.id
                return redirect('addashpat')
            if userdetail.status == '4':
                request.session['user_id'] = userdetail.id
                return redirect('addashlab')
            if userdetail.status == '5':
                request.session['user_id'] = userdetail.id
                return redirect('addashpha')
            if userdetail.status == '6':
                request.session['user_id'] = userdetail.id
                return redirect('addashbld')

        else:
            msg = 'invalid username or password'
    return render(request,'login.html', {'err_msg': msg, })
