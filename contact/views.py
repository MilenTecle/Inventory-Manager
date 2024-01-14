from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from .forms import ContactForm

# Create your views here.
def contact(request):

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, "Message successfully sent!")
            return redirect('contact')

    contact_form = ContactForm()


    return render(
        request,
        'contact/contact.html',
        {
            'contact': contact,
            'contact_form': contact_form
         },
    )

