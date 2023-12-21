from django.shortcuts import render, redirect
from .models import *
from .forms import InterviewForm
from .models import InterviewInformation
from urllib import request
from django.shortcuts import redirect, render, HttpResponse, HttpResponseRedirect
from django import template
from django.template import loader
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login , logout as auth_logout
from django.contrib.auth.decorators import login_required




def index(request):
    return render(request, 'index1.html')


def information(request):
    if request.method == 'POST':
        form = InterviewForm(request.POST, request.FILES)
        if form.is_valid():
            form_instance = form.save(commit=False)
            # Additional processing if needed before saving
            form_instance.save()
            # Redirect after successful form submission
            return redirect('questions')
        else:
            messages.error(request, "Form is invalid. Please check the details and try again.")
    else:
        form = InterviewForm()
def information(request):
    form = InterviewForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # Redirect or do something after successful form submission
            return redirect('questions')
    return render(request, 'information.html', {'form': form})

def questions(request):
    return render(request, 'questions.html')


def Cpp(request):
    return render(request, 'C++.html')

def java(request):
    return render(request, 'java.html')

def python(request):
    return render(request, 'python.html')

def clanguage(request):
    return render(request, 'C.html')

#if wanna show the saved data as a view, now no need
'''def view_saved_data(request):
    saved_data = InterviewInformation.objects.all()
    return render(request, 'saved_data.html', {'saved_data': saved_data})'''




#Login System

def login(request):
    #If user already log in
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        User_name = request.POST['User_name']
        user_pass=request.POST['user_pass']
        print(user_pass)
        user = authenticate(request, username=User_name, password=user_pass)
        print(user)
        if user is not None:
            auth_login(request, user)
            messages.success(request,"You are now logged in")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/login')
    return render(request, 'login.html')

def mysql(request):
    return render(request, 'mysql.html')

def js(request):
    return render(request, 'javascript.html')
def html(request):
    return render(request, 'html_que.html')
def Nodejs(request):
    return render(request, 'Nodejs.html')
def css(request):
    return render(request, 'css.html')

#To let ragistered user 
def ragi(request):
    #If user already log in
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        Username = request.POST['Username']
        Email = request.POST['Email']
        Password = request.POST['Password']
        confirm_pass = request.POST['confirm_pass']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        #To check user already ragistered or not
        number_check = User.objects.filter(username=Username).exists()
        email_check = User.objects.filter(email=Email).exists()

        #If user already exist
        if number_check == True:
            messages.error(request,"Your Username  Already Exists")
            return redirect('/login')
        if email_check == True:
            messages.error(request,"Your Email Already Exists")
            return redirect('/login')
        
        if Password != confirm_pass:
            messages.error(request, "Passwords do not match")
            return redirect('/ragi')
        else:
            user = User.objects.create(username=Username, email=Email, password=confirm_pass)
            user.first_name= first_name
            user.last_name = last_name
            user.set_password(confirm_pass)  # Hash the password #It's very-very imp
            user.save()
            messages.success(request, "Your Account Successfully Created")
            return redirect('/login')
    return render(request, 'ragi.html')

#For logout
def logout(request):
    try:
        auth_logout(request)
        messages.info(request, "Logged out successfully!")
        print("LOG OUT")
        return redirect('Login')

    except Exception as e:
        print("Error during logout:", str(e))
    return redirect('Home')
