from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .models import Faq

def index(request):
    if request.user.is_authenticated():
        return redirect('bankapp:account', request.user.username)
    return render(request, 'bankapp/login.html', {})

def submitLogout(request):
    logout(request)
    return redirect('bankapp:index')

def submitLogin(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
    except ():
        return render(request, 'bankapp/login.html', {'error': 'Invalid username or password'})
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('bankapp:account', username)
    else:
        return render(request, 'bankapp/login.html', {'error': 'Invalid username or password'})

def register(request):
    context = {}
    return render(request, 'bankapp/register.html', context)

def submitRegistration(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
    except ():
        render(request, 'bankapp/login.html', {'error': 'There was an error with your request'})
    if User.objects.filter(username=username).exists():
        return render(request, 'bankapp/login.html', {'error': 'Username already exists'})
    User.objects.create_user(username, email, password)
    user = authenticate(request, username=username, password=password)
    login(request, user)
    return redirect('bankapp:account', username)

def submitQuestion(request):
    try:
        question = request.POST['question']
    except ():
        return HttpResponse('Something went wrong')
    newFaq = Faq(question=question)
    newFaq.save()
    return redirect('bankapp:account', request.user.username)

def submitTransfer(request):
    try:
        to = request.POST['to']
        amount = int(request.POST['amount'])
    except ValueError:
        return account(request, username=request.user.username, error='Amount must be a number')
    user = User.objects.get(username=request.user.username)
    if user.profile.balance < amount:
        return account(request, username=request.user.username, error='Your balance is not high enough')
    if to == request.user.username:
        return account(request, username=request.user.username, error='You cannot transfer money to yourself')
    try:
        recipient = User.objects.get(username=to)
    except User.DoesNotExist:
        return account(request, username=request.user.username, error='Recipient does not exist')
    user.profile.balance -= amount
    recipient.profile.balance += amount
    user.save()
    recipient.save()
    return redirect('bankapp:account', request.user.username)

@login_required
def account(request, username, error=''):
    #todo: do something insecure with username
    user = User.objects.get(username=request.user.username)
    context = {
        'faq_list': Faq.objects.order_by('-pub_date'),
        'balance': user.profile.balance,
        'username': user.username,
        'email': user.email,
        'error': error
    }
    return render(request, 'bankapp/account.html', context)