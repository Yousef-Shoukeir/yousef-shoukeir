from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail


def home(request):
    return render(request, 'home.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        send_mail(
            name + " - " + email,
            subject,
            email,
            ['jos51ysf@gmail.com'],
            fail_silently=False,
        )

    return render(request, 'contact.html')


def projects(request):
    return render(request, 'projects.html')


def skills(request):
    return render(request, 'skills.html')


def about(request):
    return render(request, 'about.html')


def wid(request):
    return render(request, 'wid.html')
