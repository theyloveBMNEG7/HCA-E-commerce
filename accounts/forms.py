from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

# Custom user registration form
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'

# Custom authentication form for login
class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = '__all__'
