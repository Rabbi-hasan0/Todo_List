from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'yours@gmail.com', 'class': 'form-control'})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Please enter in lowercase', 'class': 'form-control'})
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     if commit:
    #         user.save()
    #     return user
class ProfileForm(forms.ModelForm):
    image = forms.ImageField(label="Upload Profile")
    class Meta:
        model = Profile
        fields = ['image']