from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Requerido')
    last_name = forms.CharField(max_length=30, required=True, help_text='Requerido')
    email = forms.EmailField(required=True, help_text='Requerido. Ingrese una dirección de email válida.')

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        )

class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
