from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
from .forms import ContactForm
from django.conf import settings


""""
Sends an email notification to the site admin and an automated reply to
the user.
The function constructs and sends an email to:
the site admin, with the details of the contact form message.
the user, with an automated reply for confirmation of recieving the message.
It also marks the contact message as read in the Django admin by setting the
'read' attribute to True.
"""


def send_contact_email(contact_instance):
    admin_subject = f"New submission from {contact_instance.name}"
    admin_body = f"Name: {contact_instance.name}\n" \
                 f"Email: {contact_instance.email}\n" \
                 f"Message: {contact_instance.message}"

    send_mail(
        admin_subject,
        admin_body,
        settings.EMAIL_HOST_USER,  # From email
        [settings.EMAIL_HOST_USER],  # Admins email
        fail_silently=False
    )

    # Automated reply to sender
    sender_subject = "Thank you for your message"
    sender_body = (" Thank you for your email, we will get back to you as "
                   "soon as possible."
                   )

    send_mail(
        sender_subject,
        sender_body,
        settings.EMAIL_HOST_USER,  # From email
        [contact_instance.email],  # Senders email
        fail_silently=False
    )

    # To automatically mark the message as read in django admin
    contact_instance.read = True
    contact_instance.save()


"""
Handles the display and submission of the contact form.
Processes the submitted data in the form and validates it.
Upon successful submission, email notifications to both the site admin
and the sender are sent. A success message is then displayed and redirects
to the contact form with a cleaned form. The messages are also displayed in
order, by latest creation at the top.
"""


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
