from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User  # Import your custom User model

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2', 'company_name', 'phone')  # Include all fields
