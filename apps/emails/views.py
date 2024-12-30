# apps/emails/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def send_email(request):
    if request.method == 'POST':
        # Email sending logic here
        messages.success(request, 'Email sent successfully!')
        return redirect('dashboard')
    return render(request, 'emails/send_email.html')

@login_required
def schedule_email(request):
    if request.method == 'POST':
        # Email scheduling logic here
        messages.success(request, 'Email scheduled successfully!')
        return redirect('dashboard')
    return render(request, 'emails/schedule_email.html')

@login_required
def email_template(request):
    templates = [
        {'name': 'Welcome Email', 'description': 'New user welcome template'},
        {'name': 'Newsletter', 'description': 'Monthly newsletter template'},
    ]
    return render(request, 'emails/email_template.html', {'templates': templates})