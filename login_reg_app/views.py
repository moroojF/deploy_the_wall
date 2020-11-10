from django.shortcuts import render, HttpResponse, redirect
from .models import Users, UserManager
from django.contrib import messages
import bcrypt

# Create your views here.
def root(request):
    return render(request, 'index.html')

def add_user(request):
    if request.method == "POST":
        errors = Users.objects.reg_validator(request.POST)

        if len(errors) > 0 :
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')

        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        birthday = request.POST['BD']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        Users.objects.create(
            first_name = fname,
            last_name=lname,
            email=email,
            password=pw_hash,
            birthday = birthday
        )
        request.session['user_id'] = Users.objects.last().id

        return redirect('/success')
    return redirect('/')

def login(request):
    if request.method == "POST":
        errors = Users.objects.login_validator(request.POST)

        if len(errors) > 0 :
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
    
        user = Users.objects.filter(email = request.POST.get('log_email'))

        if len(user) == 0: 
            messages.error(request, "Your email address is incorrect")
            return redirect('/')

        login_pswd = request.POST['log_password']

        if not bcrypt.checkpw(login_pswd.encode(), user[0].password.encode()):
            messages.error(request, "You entered wrong password!")
            return redirect ('/')

        request.session['user_id'] = Users.objects.get(email = request.POST['log_email']).id
        return redirect('/wall')
    return redirect('/')



def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    
    context = {
        'user' : Users.objects.get(id = request.session['user_id'])
    }
    return render(request, 'success.html', context)

def logout(request):

    if ('user_id' in request.session):
        del request.session['user_id']
    
    return redirect('/')