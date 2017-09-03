from django.http import HttpResponse
from django.template import loader

from .models import Faq

def index(request):
    return login(request)

def login(request):
    template = loader.get_template('bankapp/login.html')
    context = {}
    return HttpResponse(template.render(context, request))

def register(request):
    template = loader.get_template('bankapp/register.html')
    context = {}
    return HttpResponse(template.render(context, request))

def account(request):
    template = loader.get_template('bankapp/account.html')
    context = {}
    return HttpResponse(template.render(context, request))