from django.shortcuts import render, redirect
from django.core.mail import send_mass_mail
from django.conf import settings


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        new_message = f'''Please review your information!
        Name: {name}
        Email: {email}
        Message: {message}
        '''
        new_message1 = f'''Request Details
        Name: {name}
        Email: {email}
        Message: {message}
        '''

        message1 = ('Thanks for contacting us!',new_message, settings.EMAIL_HOST_USER, [email, ] )
        message2 = ('Request/Inquiry for website!',new_message1, email, [settings.EMAIL_HOST_USER, ] )

        send_mass_mail((message1, message2),fail_silently=False)
        return redirect('index')

    else:
        return render(request, 'index.html')
