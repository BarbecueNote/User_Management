from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    review_base = forms.ChoiceField(choices=CustomUser.REVIEW_BASE_CHOICES, required=True)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email','review_base', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class CustomUserEditForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    review_base = forms.ChoiceField(choices=CustomUser.REVIEW_BASE_CHOICES, required=True)
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'review_base']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

