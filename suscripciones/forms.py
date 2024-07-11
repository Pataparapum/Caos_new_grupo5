from django import forms
from django.contrib.auth.models import User

class SubscriptionForm(forms.Form):
    SUBSCRIPTION_CHOICES = [
        ('Plan Plus: Papel + Digital', 'Plan Plus: Papel + Digital'),
        ('Plan Papel Anual', 'Plan Papel Anual'),
        ('Plan Digital Anual', 'Plan Digital Anual'),
    ]
    subscription_type = forms.ChoiceField(choices=SUBSCRIPTION_CHOICES)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
