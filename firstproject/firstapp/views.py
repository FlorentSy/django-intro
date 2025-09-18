from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ReservationsForm
# Create your views here.

# Function based view


def hello_world(request):
    return HttpResponse("Hello World")


# Class based view

class HelloKosova(View):
    def get(self, request):
        return HttpResponse("Hello Kosova")


def home(request):
    form = ReservationsForm()

    if request.method == 'POST':
        form = ReservationsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success")

    return render(request, 'index.html', {'form': form})
