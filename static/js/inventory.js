document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('inventory-form');
    /*const itemsContainer = document.getElementById('items-container');
    const addItem = document.getElementById('add-item')
    const saveBtn = document.getElementById('save')*/
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    let deleteItem = null; // variable to keep track of which item to delete
    let deleteInventory = null;


    /* Handles the click event to render the inventory form */
        const toggleForm = document.getElementById('toggle-form');
        if (toggleForm) {
            toggleForm.addEventListener('click', function() {
                form.classList.toggle('hide');
                /* addItem.classList.toggle('hide')
                itemsContainer.classList.toggle('hide')
                saveBtn.classList.toggle('hide')*/
            });
        }

        /* Adding items when clicking on icon
        addItem.addEventListener('click', function() {
            const newItem = document.createElement('div');
            newItem.classList.add('item');
            newItem.innerHTML = `
                    <input type="text" name="items" class="form-control item-name" placeholder="Item name">
                    <i class="fa-solid fa-pencil edit-icon"></i>
                    <i class="fa-regular fa-trash-can delete-icon"></i>`;
            itemsContainer.appendChild(newItem); */


            /* Edit icon event listener */
            const editIcons = document.querySelectorAll('.edit-icon');
            editIcons.forEach(editIcon => {
                editIcon.addEventListener('click', function(event) {
                event.preventDefault();
                const formRow = this.closest('.form-row');
                const inputField = formRow.querySelector('.item-name');
                inputField.removeAttribute('readonly');
                inputField.focus();
            });
        });


            /* Delete icon event listener */
            const deleteIcons = document.querySelectorAll('.delete-icon');
            deleteIcons.forEach(deleteIcon => {
            deleteIcon.addEventListener('click', function(event) {
                event.preventDefault();
                deleteItem = this.dataset.itemId;
                deleteInventory = null;
                deleteModal.show();
            });
        });

            /* Delete entire list event listener */
            const deleteList = document.querySelector('.delete-list');
            if (deleteList) {
                deleteList.addEventListener('click', function() {
                    deleteInventory = this.dataset.listId;
                    deleteItem = null; // reset the variable
                    deleteModal.show();
            });
        }

        document.getElementById('deleteConfirm').addEventListener('click', function() {
            if (deleteItem) {
                document.getElementById('delete-item-form').action = `/delete_item/${deleteInventory}/${deleteItem}/`;
                document.getElementById('delete-item-form').submit();

            }
            if (deleteInventory) {
                document.getElementById('delete-list-form').action = `/delete_list/${deleteInventory}/`;
                document.getElementById('delete-list-form').submit();
            }
            deleteModal.hide();
         });
    });
