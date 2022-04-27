from django.shortcuts import render,redirect
def auth_login(func):
    def wrap(request,*args,**kwargs):
        if 'user_id' in request.session:
            return func(request,*args,**kwargs)
        else:
            return redirect('log1')
    return wrap