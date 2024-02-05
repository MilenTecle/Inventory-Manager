document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('inventory-form');
    const categoryForm = document.getElementById('category-form');
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    let deleteItem = null; // variable to keep track of which item to delete
    let deleteInventory = null;


    /* Handles the click event to render the inventory form */
        const toggleForm = document.getElementById('toggle-form');
        if (toggleForm) {
            toggleForm.addEventListener('click', function() {
                form.classList.toggle('hide');
            });
        }

          /* Handles the click event to render the category form */
          const toggleCategory = document.getElementById('toggle-category');
          if (toggleCategory ) {
              toggleCategory.addEventListener('click', function() {
                categoryForm.classList.toggle('hide');
              });
          }

            /* Edit icon event listener */
            const editIcons = document.querySelectorAll('.edit-link');
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
            const deleteIcons = document.querySelectorAll('.delete-link');
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
                document.getElementById('delete-item-form').action = `/delete_item/${deleteItem}/`;
                document.getElementById('delete-item-form').submit();

            }
            if (deleteInventory) {
                document.getElementById('delete-list-form').action = `/delete_list/${deleteInventory}/`;
                document.getElementById('delete-list-form').submit();
            }
            deleteModal.hide();
         });
    });
