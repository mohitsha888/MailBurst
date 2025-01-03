from django.db import models
from apps.accounts.models import User, ContactList

class EmailTemplate(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class EmailCampaign(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('scheduled', 'Scheduled'),
        ('sending', 'Sending'),
        ('sent', 'Sent'),
        ('failed', 'Failed')
    ]

    subject = models.CharField(max_length=200)
    content = models.TextField()

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    sent_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class EmailTracker(models.Model):
    campaign = models.ForeignKey(EmailCampaign, on_delete=models.CASCADE)
    recipient = models.EmailField()
    opened = models.BooleanField(default=False)
    opened_at = models.DateTimeField(null=True, blank=True)
    clicked = models.BooleanField(default=False)
    clicked_at = models.DateTimeField(null=True, blank=True)
    bounced = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)