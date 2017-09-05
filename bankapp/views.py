from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .models import Faq

def index(request):
    template = loader.get_template('bankapp/login.html')
    context = {}
    return HttpResponse(template.render(context, request))

def submitLogout(request):
    logout(request)
    return redirect('bankapp:index')

def submitLogin(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
    except ():
        return HttpResponse('Something went wrong')
    return login_and_redirect_to_account(request, username, password)

def register(request):
    template = loader.get_template('bankapp/register.html')
    context = {}
    return HttpResponse(template.render(context, request))

def submitRegistration(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
    except ():
        return HttpResponse('Something went wrong')
    #No validation of whether the user exists
    User.objects.create_user(username, email, password)
    return login_and_redirect_to_account(request, username, password)

def submitQuestion(request, question):
    return HttpResponse("submitting question %s" % question)

@login_required
def account(request, username):
    template = loader.get_template('bankapp/account.html')
    context = {}
    return HttpResponse(template.render(context, request))

def login_and_redirect_to_account(request, username, password):
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('bankapp:account', username)
    else:
        return redirect('bankapp:register')