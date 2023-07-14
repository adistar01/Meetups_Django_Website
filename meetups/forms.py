from django import forms

#from .models import Participant

#class RegistrationForm(forms.ModelForm):
#    class Meta:
#        model = Participant
#        fields = '__all__'

class RegistrationForm(forms.Form):
    email = forms.EmailField(label="Your email")