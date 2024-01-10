from django.shortcuts import render
from django.contrib import messages
from .models import Contact
from .forms import ContactForm

# Create your views here.
def contact(request):

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            print('Before message')
            messages.add_message(request, messages.SUCCESS, "Message successfully sent!")
            print('after message')
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

