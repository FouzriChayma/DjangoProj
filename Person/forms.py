from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Person

class RegisterForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ("username", "email", "cin","first_name","last_name", "password1", "password2")
    
    def save(self, commit=True):
        return super(RegisterForm, self).save(commit=commit)  # missing =commit
