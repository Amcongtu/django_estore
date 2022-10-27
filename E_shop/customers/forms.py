from django import forms
from customers.models import Customer


class FormSignUpCustomer(forms.ModelForm):
    fullname = forms.CharField(label='Full name', max_length=100, widget=forms.TextInput(attrs={
        'class': 'modal-input',
        'placeholder': 'Full name',
    }))
    phone_number = forms.CharField(label='Điện thoại', max_length=20, widget=forms.TextInput(attrs={
        'class': ' modal-input',
        'placeholder': 'Phone number',
    }))
    email = forms.EmailField(label='Email', max_length=200, widget=forms.EmailInput(attrs={
        'class': 'model-account modal-input',
        'placeholder': 'Email',
    }))
    password = forms.CharField(label='Mật khẩu', max_length=150, widget=forms.PasswordInput(attrs={
        'class': 'model-account modal-input',
        'placeholder': 'Password',
    }))
    password2 = forms.CharField(label='Xác nhận Mật khẩu', max_length=150, widget=forms.PasswordInput(attrs={
        'class': 'model-account modal-input',
        'placeholder': 'Re-enter the password',
    }))



    class Meta:
        model = Customer
        fields = ['fullname','phone_number',  'email', 'password', 'password2']

        # fields = '__all__'

    # class Meta:
    #     model = Customer
    #     exclude = ['ngay_tao']

