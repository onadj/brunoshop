from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.contrib import messages
# Create your views here.


def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            messages.success(request, 'Thanks \
                we recived your email and will contact you shortly.')
            try:
                send_mail(from_email, message, subject, [
                          'brunowebshop666@gmail.com'])

            except BadHeaderError:
                return HttpResponse('invalid header')

    else:
        form = ContactForm()

    context = {
        'form': form
    }

    return render(request, 'contact/contact.html', context)
