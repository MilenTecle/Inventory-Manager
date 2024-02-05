from django.db import IntegrityError
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
            try:
                # User can create new category
                category_name = inventory_form.cleaned_data['category']
                category, created = Category.objects.get_or_create(name=category_name)

                # Create the inventory list and link to the category
                inventory_list = inventory_form.save(commit=False)
                inventory_list.user = request.user
                inventory_list.category = category

                inventory_list.save()
                messages.success(request, "Inventory created successfully!")
                return redirect('inventory_detail', pk=inventory_list.pk)
            except IntegrityError:
                messages.error(request, "An inventory with that name already exists. Please choose a different name")

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
                if not inventory.items.exists():
                    messages.error(request, "You need to add at least one item before saving list.")
                else:
                    messages.success(request, "Item added successfully!")
                return redirect('inventory_detail', pk=inventory.pk)
            elif 'save' in request.POST:
                if not inventory.items.exists():
                    messages.error(request, "You cannot save an empty list.")
                else:
                    messages.success(request, "List saved successfully!")
                    return redirect('inventory')

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
            messages.success(request, "List updated successfully")
            return redirect('inventory_detail', pk=item.inventory.pk)
    return redirect('inventory_detail', pk=item.inventory.pk)



@login_required
def clone_item(request, item_id):
    print(f"serch id {item_id} --")
    inventory = get_object_or_404(Inventory, pk=item_id, user=request.user)
    if request.method == 'POST':
        formset = ItemFormset(request.POST, instance=inventory)
        print(f'show post {formset}')
        if formset.is_valid():
            item_list = formset.save(commit=False)
            inventory = item_list[0].inventory
            new_inventory = Inventory(user=request.user, name=inventory.name + ' cloned', category=inventory.category)
            new_inventory.save()
            for item in item_list:
                new_item = Items(name=item.name, inventory=new_inventory)
                new_item.save()
            for item in inventory.items.all():
                new_item = Items(name=item.name, inventory=new_inventory)
                new_item.save()
            messages.success(request, "List cloned successfully")
            return redirect('inventory_detail', pk=new_inventory.pk)
        else:
            print(formset.errors)
    else:
        formset = ItemFormset(instance=inventory)
    return render(request, 'inventory/inventory_clone.html', {
        'inventory': inventory,
        'formset': formset
    })




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

