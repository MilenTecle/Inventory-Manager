/* Handles the click event to render the inventory form */

document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('inventory-form');
    document.getElementById('toggle-form').addEventListener('click', function() {
        form.classList.toggle('hide');
    });
});