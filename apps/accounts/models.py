from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    company_name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

 # Avoid reverse accessor clashes
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",
        blank=True,
        help_text=_("The groups this user belongs to."),
        verbose_name=_("groups"),
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",
        blank=True,
        help_text=_("Specific permissions for this user."),
        verbose_name=_("user permissions"),
    )

class ContactList(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    contact_list = models.ForeignKey(ContactList, on_delete=models.CASCADE)
    subscribed = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)