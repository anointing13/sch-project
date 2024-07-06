from django.shortcuts import render

from .forms import ContactForm
from .models import Contact


# Create your views here.

def contact(request):
    message = ""
    product = Contact.objects.all()
    forms = ContactForm

    if request.method == "POST":
        forms = ContactForm(request.POST)
        if forms.is_valid():
            forms.save()
            request.POST = ""
            message = "Message Sent Successfully"
        else:
            message = "Message Not Sent"

    return render(request, 'contact/contact.html', {'key': product, 'form': forms, 'message': message})