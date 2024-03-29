from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages
from .forms import InventoryForm, ItemsForm, ItemFormset, CategoryForm
from .models import Inventory, Items, Category


"""
Render the privacy policy page
"""


def privacy_policy(request):
    return render(request, 'privacy_policy.html')


"""
If a user is authenticated they are redirected to their inventory page
(the dashboard), otherwise it renders the landing page, the start page for
unauthenticated or logged out users.
"""


def landing_page(request):
    # Check if the user is authenticated.
    if request.user.is_authenticated:
        return redirect('inventory')
    return render(request, 'landing_page.html')


"""
Display a form for adding categories and display existing categories.
POST requests, it attempts to add a new category based on the submitted data.
It validates the form and if the form is valid, saves the form and provides
success or errror feedback to user. Redirects to category page where the
category along with existing ones will be displayed.
"""


@login_required(login_url='/accounts/login/')
def add_category(request):
    # Initialize an empty category form.
    category_form = CategoryForm()
    # Fetch all categories belonging to the current user, ordered by name.
    categories = Category.objects.filter(user=request.user).order_by('name')

    if request.method == 'POST':
        category_form = CategoryForm(request.POST)

        if category_form.is_valid():
            try:
                # Prepare the the category instance but not save it yet.
                category = category_form.save(commit=False)
                category.user = request.user
                category.save()
                messages.success(request, "Category added successfully")
                return redirect("add_category")
            except IntegrityError:
                messages.error(
                    request, "A category with that name already exists."
                    "Please choose a different name.")
    else:
        category_form = CategoryForm()

    return render(request, 'inventory/categories.html', {
        'category_form': category_form,
        'categories': categories
    })


"""
Deletes a specific category identified by category_id.
Fetches the category by its ID and deletes it. Upon successful deletion,
it redirects to the category page with a success message, or else an error
message will be displayed.
"""


@login_required
def delete_category(request, category_id):
    # Retrieve the category to be deleted or show 404 if not found.
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.delete()
        messages.success(request, "Category deleted successfully")
        return redirect("add_category")
    else:
        messages.error(request, "The category could not be deleted")
    return redirect("add_category")


"""
Allow user to edit the category's name with inline editing
(without leaving the page) When form is submitted (POST request), it attempts
to update the category with the new category name. Validation errors and
uniqueness constraints are handled with appropiate feedback.
Upon successful update, it redirects user back to the category page.
"""


@login_required
def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        # Populate the form with POST data and the instance to be updated.
        form = CategoryForm(data=request.POST, instance=category)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Category updated successfully")
                return redirect("add_category")
            except IntegrityError:
                messages.error(request, "The category name already exists, "
                               "please choose another name.")
        else:
            messages.error(request, "The category could not be edited")
    return redirect("add_category")


"""
The initial form were user creates a new inventory list.
POST request, it processes the form data to create the new inventory and
handling validation and uniqueness constraints with appropiate feedback. Upon
succesful submission, the user gets redirected to the inventory detail view
for addition of the items, otherwise the page re-renders with an error
message.
"""


@login_required(login_url='/accounts/login/')
def inventory_page(request):
    # Fetch all inventories owned by the user, sorted by name.
    inventories = Inventory.objects.filter(user=request.user).order_by('name')
    inventory_form = InventoryForm(user=request.user)

    if request.method == 'POST':
        inventory_form = InventoryForm(data=request.POST, user=request.user)
        if inventory_form.is_valid():
            try:
                # Inventory instance is prepared but not saved.
                inventory_list = inventory_form.save(commit=False)
                inventory_list.user = request.user

                inventory_list.save()
                messages.success(request, "Inventory created successfully!")
                return redirect('inventory_detail', pk=inventory_list.pk)
            except IntegrityError:
                messages.error(request, "An inventory with that name already "
                               "exists. Please choose a different name")

    return render(request, 'inventory/inventory.html', {
        'inventory_form': inventory_form,
        'inventories': inventories
    })


"""
The view where the user can see the specific items in the inventory list,
including editing and adding items. Shows the details of an inventory,
identified byt its primary key (pk), and its associated items. The view
handles the viewing of items and the submission of new or edited items
(through an inline formset). Depending on the action, 'add_item' and 'save',
it validates and saves new items to the inventory, updates existing items and
provides feedback upon error or success. Redirects to inventory page
(dashbord) upon success or re-renders page if errors.
"""


def inventory_detail(request, pk):
    # Retrieve the specific inventory instance by pk or return a 404
    inventory = get_object_or_404(Inventory, pk=pk, user=request.user)
    formset = ItemFormset(request.POST, instance=inventory)
    inventory_form = InventoryForm(
        request.POST,
        instance=inventory,
        user=request.user
        )
    category_dropdown = True

    if request.method == 'POST':
        # Check if inventory form and formset are valid.
        if inventory_form.is_valid():
            inventory_form.save()
        # Track the initial count of items to compare after updates
        item_count = inventory.items.count()

        if formset.is_valid():
            instances = formset.save()

            if 'add_item' in request.POST:
                # Recount items if added
                new_item_count = inventory.items.count()
                # Check if new items were added
                if new_item_count > item_count:
                    messages.success(request, "Item added successfully!")
                else:
                    messages.error(request, "No item was added.")
                return redirect('inventory_detail', pk=inventory.pk)
            elif 'save' in request.POST:
                if not inventory.items.exists():
                    messages.error(request, "You cannot save an empty list.")
                    return redirect('inventory_detail', pk=inventory.pk)
                else:
                    formset.save()
                    messages.success(request, "List saved successfully!")
                return redirect('inventory')

    else:
        formset = ItemFormset(instance=inventory)
        inventory_form = InventoryForm(instance=inventory, user=request.user)

    return render(request, 'inventory/inventory_detail.html', {
        'inventory': inventory,
        'formset': formset,
        'category_dropdown': category_dropdown,
        'inventory_form': inventory_form,
    })


"""
Deletes a specific item from an inventory list.
Fetches an item by its ID, verifies user, deletes the item and redirects the
user back to the inventory detail page with a success message.
"""


@login_required
def delete_item(request, item_id):
    if request.method == 'POST':
        # Retrieve the item to be deleted & ensure it belongs to current user
        item = get_object_or_404(
            Items,
            id=item_id,
            inventory__user=request.user
            )
        inventory_id = item.inventory.pk
        item.delete()
        messages.success(request, "Item deleted successfully!")
        return redirect('inventory_detail', pk=inventory_id)
    else:
        messages.error(request, "Could not delete item.")
        return redirect('inventory_detail', pk=inventory_id)


"""
Deletes an entire inventory list, including all the items identified by pk.
Retrieves the inventory by its pk, verifies that user and then deletes the
inventory list with all associated items. Redirects the user back to the the
inventory page (the dashboard) with a success message.
"""


@login_required
def delete_list(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk, user=request.user)
    if request.method == 'POST':
        inventory.delete()
        messages.success(request, "Inventory list deleted successfully!")
        return redirect('inventory')


"""
Clones an existing inventory list and its items, allowing addition of new
items. Creates a copy of an inventory list, identified by item_id, including
all its times. The user can also add new items before saving the list. Handles
uniqueness of inventory name by appending 'cloned' to the original name.
Provides feedback upon successful cloning or appropiate error message. Upon
successful cloning, redirects user to the inventory page (dashboard), and
depending on the error, the user stays on the page with error message or gets
redireted to the dashboard.
"""


@login_required
def clone_list(request, item_id):
    inventory = get_object_or_404(Inventory, pk=item_id, user=request.user)
    cloned_inventory_name = f"{inventory.name} cloned"
    category_dropdown = True

    """ Checks if the inventory has already been cloned before processing the
    form
    """
    # Prevents cloning if a clone with the same name already exists
    if Inventory.objects.filter(
            user=request.user,
            name=cloned_inventory_name).exists():
        messages.error(request, "This inventory has already been cloned.")
        return redirect('inventory')

    if request.method == 'POST':
        formset = ItemFormset(request.POST, instance=inventory)
        inventory_form = InventoryForm(
            request.POST,
            instance=inventory,
            user=request.user
            )

        # Checks if an item was added or not
        if 'add_item' in request.POST:
            if formset.is_valid():
                item_list = formset.save(commit=False)

                if not item_list:
                    messages.error(request, "No new item was added.")
                    return redirect('clone_list', item_id=item_id)
                else:
                    formset.save()
                    messages.success(request, "Item added successfully!")
                    return redirect('clone_list', item_id=item_id)

        elif inventory_form.is_valid() and formset.is_valid():
            item_list = formset.save(commit=False)
            # Create a new inventory instance for the cloned inventory
            new_inventory = Inventory(
                user=request.user,
                name=cloned_inventory_name,
                category=inventory.category
                )
            new_inventory.save()
            for item in item_list:
                new_item = Items(name=item.name, inventory=new_inventory)
                new_item.save()
            for item in inventory.items.all():
                new_item = Items(name=item.name, inventory=new_inventory)
                new_item.save()
            messages.success(request, "List cloned successfully")
            return redirect('inventory')
        else:
            print(formset.errors)
    else:
        formset = ItemFormset(instance=inventory)
        inventory_form = InventoryForm(instance=inventory, user=request.user)

    return render(request, 'inventory/inventory_clone.html', {
        'inventory': inventory,
        'formset': formset,
        'inventory_form': inventory_form,
        'category_dropdown': category_dropdown,
    })


"""
Displays a static view of a specific inventory list with its items for
sharing. Includes the option to click on delete och edit list but only for
the list owner. Fetches an inventory by its ID and displays a read-only list
of the items, excluding the edit and delete functionality when shared.
"""


def saved_list(request, inventory_id):
    inventory = get_object_or_404(Inventory, id=inventory_id)
    # Check if the current user is the owner of the inventory
    is_owner = request.user == inventory.user
    context = {
        'inventory': inventory,
        'is_owner': is_owner,
    }
    return render(request, 'inventory/saved_list.html', context)
