from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from .forms import InventoryForm, ItemsForm
from .models import Inventory, Items
from django.http import HttpResponseRedirect

# Create your views here.
def landing_page(request):
    return render(request, 'landing_page.html')

def inventory_page(request):
    if request.method == 'POST':
        list = InventoryForm(request.POST)
        if list.is_valid():
           inventory_list = list.save(commit=False)
           inventory.list.save()
           return redirect('inventory_detail', pk=inventory_list.pk)
    else:
        list = InventoryForm()
    return render(request, 'inventory/inventory.html', {'list': list})
