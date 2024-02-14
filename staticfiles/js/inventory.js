document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('inventory-form');
    const categoryForm = document.getElementById('category-form');
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    let deleteItem = null; // variable to keep track of which item to delete
    let deleteInventory = null; // variable to keep track of which inventory to delete
    let deleteCategory = null; // variable to keep track of which category to delete


    /* Toggles the visibility of the inventory form by clicking on the icon */
        const toggleForm = document.getElementById('toggle-form');
        if (toggleForm) {
            toggleForm.addEventListener('click', function() {
                form.classList.toggle('hide');
            });
        }

          /* Toggles the visibility of the category form by clicking on the icon */
          const toggleCategory = document.getElementById('toggle-category');
          if (toggleCategory ) {
              toggleCategory.addEventListener('click', function() {
                categoryForm.classList.toggle('hide');
              });
          }

            /* Edit icon event listener. Enables inline editing of items by remonving the 'readonly' attribute */
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


            /* Delete icon event listener. Prepares deletion of items by setting up the delete modal with item-specific data */
            const deleteIcons = document.querySelectorAll('.delete-link');
            deleteIcons.forEach(deleteIcon => {
            deleteIcon.addEventListener('click', function(event) {
                event.preventDefault();
                deleteItem = this.dataset.itemId;
                deleteInventory = null;
                deleteModal.show();
            });
        });



            /* Delete categories event listener. Prepares deletion of categories by setting up the delete modal with category-specific data */
            const deleteCategories = document.querySelectorAll('.delete-category-link');
            deleteCategories.forEach(button => {
            button.addEventListener('click', function(event) {
                event.preventDefault();
                deleteCategory = this.getAttribute('data-category-id');
                deleteItem = null;
                deleteModal.show();
            });
        });


           /* Edit categories event listener with inline editing, by removing the 'readonly' attribute and display the save button */
           const editCategories = document.querySelectorAll('.edit-category-link');
           editCategories.forEach(button => {
               button.addEventListener('click', function(event) {
                event.preventDefault();
                const categoryContainer = this.closest('.category-container');
                const inputField = categoryContainer.querySelector('.category-name');
                const saveBtn = categoryContainer.querySelector('.save-link');
                inputField.removeAttribute('readonly');
                inputField.focus();
                saveBtn.classList.remove('hide');
                });
            });


           /* Save button event listener. Submits the category form that is associated with the save button to get the changes made */
           document.querySelectorAll('.save-link').forEach(saveBtn => {
            saveBtn.addEventListener('click', function(event) {
                event.preventDefault();
                const form = this.closest('form');
                form.submit();
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

        /* Confirm the deletion action based on the type to be deleted, item, inventory or category */
        document.getElementById('deleteConfirm').addEventListener('click', function() {
            if (deleteItem) {
                document.getElementById('delete-item-form').action = `/delete_item/${deleteItem}/`;
                document.getElementById('delete-item-form').submit();

            }
            if (deleteInventory) {
                document.getElementById('delete-list-form').action = `/delete_list/${deleteInventory}/`;
                document.getElementById('delete-list-form').submit();
            }

            if(deleteCategory) {
                document.getElementById('delete-category-form').action = `/delete_category/${deleteCategory}/`;
                document.getElementById('delete-category-form').submit();
            }
            deleteModal.hide();
         });
    });

