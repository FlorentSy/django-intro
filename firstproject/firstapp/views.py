from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

#Function based view
def hello_world(request):
    return HttpResponse("Hello World")


#Class based view

class HelloKosova(View):
    def get(self, request):
        return HttpResponse("Hello Kosova")