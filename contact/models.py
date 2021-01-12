from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your models here.


def contact(request):
    if request.method == "POST":
        message_email = request.POST['message-email']
        message = request.POST['message']
        message_name = request.POST['message-name']

        messages.success(request, 'Thanks \
                I recived your email and  I will contact you shortly.')

        send_mail(
            message_email,
            message,
            message_name,
            ['onagydentalproject@gmail.com'],
            fail_silently=False,
        )

        return render(request, 'contact.html', {'message_name ': message_name})
    else:
        return render(request, 'contact.html', {})
