from django.http import HttpResponse
from django.shortcuts import redirect, render
from todoApp.models import Users
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError

# Create your views here.

def home(request):
    return render(request, 'registration/home.html')

def signup(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName');
        lastName = request.POST.get('lastName');
        email = request.POST.get('email');
        password = request.POST.get('password');
        print(password)
        # hashed_password = make_password(password)
        # print(hashed_password)
        Users.objects.create(firstName=firstName, lastName=lastName, email=email, password=password)
        messages.add_message(request, messages.INFO, 'Your account created successfully!')
        return redirect('/userlogin')
    return render(request, 'registration/signup.html')
 
def userlogin(request):
    if request.method == 'POST':
        email = request.POST.get('email');
        password = request.POST.get('password');
        print("Email",email)
        print("Password", password)
        # hashed_password = make_password(password)
        # print("Hashed_password:", hashed_password)
        user = authenticate(request, email = email, password = password)      
        if user is not None:
            login(request, user)
            return redirect('/')  
        else:
            return HttpResponse ("Username or password is incorrect !")
            # return redirect('/userlogin')
    return render(request, 'registration/login.html')

def todopage(request):
    return render(request, 'registration/todopage.html')
       