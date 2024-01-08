from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def landing_page(request):
    return render(request, 'inventory/landing_page.html')