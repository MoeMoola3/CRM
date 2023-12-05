from django import forms
from .models import Lead

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent',
        )

# Old Way
class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)


"""
FORMS
Definition: Forms are Python classes that define how data should be collected and validated from the user.
Responsibility: Forms handle user input, validate data, and provide a convenient way to interact with HTML forms.
"""