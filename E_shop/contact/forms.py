from django import forms
from contact.models import  Contact

class FormContact(forms.ModelForm):
    name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'class': 'control-group--input',
        'placeholder': 'Full name',
        "id":"name",
        "required":"required",
        "data-validation-required-message": "Please enter your name",
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'control-group--input',
        'placeholder': 'Your Email',
        'id':"email",
        "data-validation-required-message":"Please enter your email",
        "required":"required" ,
    }))
    subject = forms.CharField(max_length=264, widget=forms.TextInput(attrs={
        'class': 'control-group--input',
        'placeholder': 'Subject',
        'id':"subject",
        'required':"required",
        'data-validation-required-message':"Please enter a subject",
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'control-group--texbox',
        'placeholder': 'Message',
        'rows': '6',
        'id':"message",
        'required':"required",
        'data-validation-required-message':"Please enter your message",
    }))


    class Meta:
        model = Contact
        exclude = ('send_day',)