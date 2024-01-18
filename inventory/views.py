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
            messages.success(request, "Inventory list saved successfully!")
            return redirect('inventory')

    return render(request, 'inventory/inventory.html', {
        'inventory_form': inventory_form,
        'inventories': inventories
    })

# The view where the user can see the specific items in the inventory list
def inventory_detail(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk, user=request.user)
    if request.method == 'POST':
        formset = ItemFormset(request.POST, instance=inventory)
        if formset.is_valid():
            formset.save()
            messages.success(request, "Item added successfully!")
            return redirect('inventory_detail', pk=inventory.pk)

    else:
            formset = ItemFormset(instance=inventory)

    return render(request, 'inventory/inventory_detail.html', {
        'inventory': inventory,
        'formset': formset
    })


@login_required
def delete_item(request, item_id):
     item = get_object_or_404(Items, id=item_id, user=request.user)
     if request.method == 'POST':
        item.delete()
        messages.success(request, "Item deleted successfully")
        return redirect('inventory_detail', pk=item.inventory.pk)


@login_required
def edit_item(request, item_id):
    item = get_object_or_404(Items, id=item_id, inventory__user=request.user)

    if request.method == 'POST':
        form = ItemsForm(data=request.POST, instance=items)
        if form.is_valid():
            form.save()
            messages.success(request, "Item updated successfully")
            return redirect('inventory_detail', pk=item.inventory.pk)
    else:
        form = ItemsForm(instance=item)

    return render(request, 'inventory/edit_inventory.html', {'form': form, 'item': item})



def dashboard(request):
    return render(request, 'inventory/inventory.html', {'inventories': inventories})

