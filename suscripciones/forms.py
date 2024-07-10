from django import forms

class SubscriptionForm(forms.Form):
    TYPE_CHOICES = [
        ('mensual', 'Mensual  $2.500'),
        ('semestral', 'Semestral  $10.000'),
        ('anual', 'Anual  $25.000'),
    ]
    subscription_type = forms.ChoiceField(choices=TYPE_CHOICES, label='Tipo de Suscripción')
