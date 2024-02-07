document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('inventory-form');
    const categoryForm = document.getElementById('category-form');
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    let deleteItem = null; // variable to keep track of which item to delete
    let deleteInventory = null;
    let deleteCategory = null;


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



            /* Delete categories event listener */
            const deleteCategories = document.querySelectorAll('.delete-category-link');
            deleteCategories.forEach(button => {
            button.addEventListener('click', function(event) {
                event.preventDefault();
                deleteCategory = this.getAttribute('data-category-id');
                deleteItem = null;
                deleteModal.show();
            });
        });


           /* Edit categories event listener with inline editing and display the save button*/
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


           /* Save button event listener */
           document.querySelectorAll('.save-link').forEach(saveBtn => {
            saveBtn.addEventListener('click', function() {
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

        document.getElementById('deleteConfirm').addEventListener('click', function() {
            if (deleteItem) {
                document.getElementById('delete-item-form').action = `/delete_item/${deleteItem}/`;
                document.getElementById('delete-item-form').submit();

            }
            if (deleteInventory) {
                document.getElementById('delete-list-form').action = `/delete_category/${deleteCategory}/`;
                document.getElementById('delete-list-form').submit();
            }

            if(deleteCategory) {
                document.getElementById('delete-category-form').action = `/delete_category/${deleteCategory}/`;
                document.getElementById('delete-category-form').submit();
            }
            deleteModal.hide();
         });
    });

