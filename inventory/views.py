from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages
from .forms import InventoryForm, ItemsForm, ItemFormset
from .models import Inventory, Items, Category
from django.http import HttpResponseRedirect

# Create your views here.
def landing_page(request):
    return render(request, 'landing_page.html')

@login_required(login_url='/accounts/login/')
def inventory_page(request):
    inventories = Inventory.objects.filter(user=request.user)
    inventory_form = InventoryForm()

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
            messages.success(request, "Inventory created successfully !")
            return redirect('inventory_detail', pk=inventory_list.pk)

    return render(request, 'inventory/inventory.html', {
        'inventory_form': inventory_form,
        'inventories': inventories
    })

# The view where the user can see the specific items in the inventory list
def inventory_detail(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk, user=request.user)
    formset = ItemFormset(request.POST, instance=inventory)


    if request.method == 'POST':
        if formset.is_valid():
            formset.save()
            if 'add_item' in request.POST:
                messages.success(request, "Item added successfully!")
                return redirect('inventory_detail', pk=inventory.pk)
            elif 'save' in request.POST:
                messages.success(request, "List saved successfully!")
                return redirect('saved_list', inventory_id=inventory.pk)

    else:
            formset = ItemFormset(instance=inventory)

    return render(request, 'inventory/inventory_detail.html', {
        'inventory': inventory,
        'formset': formset
    })


@login_required
def delete_item(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(Items, id=item_id, inventory__user=request.user)
        inventory_id = item.inventory.pk
        item.delete()
        messages.success(request, "Item deleted successfully")
        return redirect('inventory_detail', pk=inventory_id)


@login_required
def delete_list(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk, user=request.user)
    if request.method == 'POST':
     inventory.delete()
     messages.success(request, "Inventory list deleted successfully")
     return redirect('inventory')


@login_required
def edit_item(request, item_id):
    item = get_object_or_404(Items, id=item_id, inventory__user=request.user)

    if request.method == 'POST':
        form = ItemsForm(data=request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Item updated successfully")
            return redirect('inventory_detail', pk=item.inventory.pk)
    return redirect('inventory_detail', pk=item.inventory.pk)


def saved_list(request, inventory_id):
    inventory = get_object_or_404(Inventory, id=inventory_id)
    is_owner = request.user == inventory.user
    context = {
        'inventory': inventory,
        'is_owner': is_owner,
    }
    return render(request, 'inventory/saved_list.html', context)


def dashboard(request):
    return render(request, 'inventory/inventory.html', {'inventories': inventories})

