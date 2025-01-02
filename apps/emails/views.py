from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from datetime import datetime

from mailburst import settings
from .models import EmailCampaign
#from django.http import HttpResponseBadRequest

from django.core.mail import EmailMessage

@login_required
def create_campaign(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        content = request.POST.get('content')
        recipient_list_str = request.POST.get('recipient_list')

        try:
            campaign = EmailCampaign.objects.create(
                subject=subject,
                content=content,
                status='sending'
            )

            recipient_list = [email.strip() for email in recipient_list_str.split(',') if email.strip()]
            
            # Create EmailMessage object
            email = EmailMessage(
                subject=subject,
                body=content,
                from_email=settings.EMAIL_HOST_USER,
                bcc=recipient_list,  # Using BCC instead of recipient_list
                reply_to=['ms1247031noreply@gmail.com'],  
            )
            
            email.send(fail_silently=False)

            campaign.status = 'sent'
            campaign.sent_at = datetime.now()
            campaign.save()
            
            messages.success(request, f'Email sent to {len(recipient_list)} recipients')
            return redirect('dashboard')

        except Exception as e:
            campaign.status = 'failed'
            campaign.save()
            messages.error(request, str(e))
            return render(request, 'emails/send_email.html')

    return render(request, 'emails/send_email.html')

@login_required
def schedule_email(request):
    if request.method == 'POST':
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