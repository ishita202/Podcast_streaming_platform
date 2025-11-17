from django import forms
from .models import SubscriptionPlan

class SubscriptionForm(forms.Form):
    plan = forms.ModelChoiceField(
        queryset=SubscriptionPlan.objects.all(),
        widget=forms.RadioSelect,
        empty_label=None  # Removes "------" option
    )
