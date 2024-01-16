from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Login

# def login(request):
#     return HttpResponse("Hello world!")


# def login(request):
#   template = loader.get_template('myfirst.html')
#   return HttpResponse(template.render())


def login(request):
  mylogin = Login.objects.all().values()
  template = loader.get_template('all_login.html')
  context = {
    'mylogin': mylogin,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mylogin = Login.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mylogin': mylogin,
  }
  return HttpResponse(template.render(context, request))