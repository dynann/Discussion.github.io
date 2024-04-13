from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms
from crispy_forms.helper import FormHelper

class UserCreation(UserCreationForm):
    girlfriend = forms.IntegerField()
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'girlfriend', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Remove password validation messages
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['username'].help_text = None
        
        


class PasswordChangeForm(UserChangeForm):
    # ... your form fields and logic ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_errors = False
        self.fields['new_password1'].help_text = None
        self.fields['new_password2'].help_text = None
            