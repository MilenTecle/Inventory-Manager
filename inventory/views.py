from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages
from .forms import InventoryForm, ItemsForm
from .models import Inventory, Items, Category
from django.http import HttpResponseRedirect

# Create your views here.
def landing_page(request):
    return render(request, 'landing_page.html')

@login_required(login_url='/accounts/login/')
def inventory_page(request):
    if request.method == 'POST':
        inventory_form = InventoryForm(data=request.POST)
        if inventory_form.is_valid():
            # User can create category
            category_name = inventory_form.cleaned_data['category']
            category, created = Category.objects.get_or_create(name=category_name)

            # Create the inventory list and link to the category
            inventory_list = inventory_form.save(commit=False)
            inventory_list.user = request.user
            inventory_list.category = category
            inventory_list.save()
            messages.success(request, "Inventory list saved successfully!")
            return redirect('dashboard')
    else:
        inventory_form = InventoryForm()
    return render(request, 'inventory/inventory.html', {'inventory_form': inventory_form})


def inventory_detail(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)

    return render(request, 'inventory/inventory_detail.html', {'inventory': inventory})

def dashboard(request):
    inventories = Inventory.objects.filter(user=request.user)
    return render(request, 'inventory/dashboard.html', {'inventories': inventories})
