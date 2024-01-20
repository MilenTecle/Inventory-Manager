from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from .models import Contact
from .forms import ContactForm
from django.conf import settings

# Create your views here.
def contact(request):

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_instance = contact_form.save()
            send_contact_email(contact_instance)
            messages.success(request, "Message successfully sent!")
            return redirect('contact')

    new_message = Contact.objects.all().order_by('-created_at').first()
    contact_form = ContactForm()


    return render(
        request,
        'contact/contact.html',
        {
            'new_message': new_message,
            'contact_form': contact_form
         },
    )

def send_contact_email(contact_instance):
    subject = f"New submission from {contact_instance.name}"
    email_message = f"Name: {contact_instance.name}\nEmail: {contact_instance.email}\nMessage: {contact_instance.message}"
    from_email = settings.EMAIL_HOST_USER
    recipient_email = settings.EMAIL_HOST_USER


    email = EmailMessage(
        subject,
        email_message,
        from_email,
        [recipient_email],
        reply_to=[contact_instance.email]
    )
    email.send(fail_silently=False,)
