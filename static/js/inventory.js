document.addEventListener('DOMContentLoaded', function () {
const form = document.getElementById('inventory-form');
const itemsContainer = document.getElementById('items');
const addItem = document.getElementById('add-item')



/* Handles the click event to render the inventory form */
    document.getElementById('toggle-form').addEventListener('click', function() {
        form.classList.toggle('hide');;
        addItem.classList.toggle('hide')
    });


    /* Adding items when clicking on icon */
    addItem.addEventListener('click', function() {
        const newItem = document.createElement('div');
        newItem.classList.add('item');
        newItem.innerHTML = `
                <input type="text" name="items" class="form-control item-name" placeholder="Item name">
                <i class="fa-solid fa-pencil edit-icon"></i>
                <i class="fa-regular fa-trash-can delete-icon"></i>`;
        itemsContainer.appendChild(newItem);


        /* Edit icon event listener */
        const editIcon = newItem.querySelector('.edit-icon');
        editIcon.addEventListener('click', function() {
            const inputField = newItem.querySelector('.item-name');
            inputField.removeAttribute('readonly');
            inputField.focus();
        });

        /* Delete icon event listener */
        const deleteIcon = newItem.querySelector('.delete-icon');
        deleteIcon.addEventListener('click', function() {
            newItem.remove();
        });
    });
});