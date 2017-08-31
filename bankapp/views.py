from django.http import HttpResponse
from django.template import loader

from .models import Faq


def index(request):
    return HttpResponse("Hello, world. You're at the bankapps index.")

def login(request):
    template = loader.get_template('bankapp/login.html')
    context = {}
    return HttpResponse(template.render(context, request))