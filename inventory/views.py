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
            # User can create category
            category_name = list.cleaned_data['category']
            category, created = Category.objects.get_or_create(name=category_name)

            # Create the inventory list and link to the category that
            inventory_list = list.save(commit=False)
            inventory_list.user = request.user
            inventory_list.category = category
            inventory_list.save()
            return redirect('inventory_detail', pk=inventory_list.pk)
    else:
        list = InventoryForm()
    return render(request, 'inventory/inventory.html', {'list': list})
