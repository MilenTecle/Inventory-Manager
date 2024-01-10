from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(request, messages.SUCCESS, "Message successfully sent!")
            # Clears the form
            contact_form = ContactForm()


    return render(
        request,
        'contact/contact.html',
        {
            "contact": contact,
            'contact_form': contact_form
         },
    )

