
from django import forms
from .models import Users
from django.contrib import auth

class LoginForm(forms.Form):
    username = forms.CharField(label="Username",
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password", 
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}),)
    
    
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        user = auth.authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError("Invalid username and Password")
        return user
        
        
class RegisterForm(forms.Form, ):
    firstname = forms.CharField(required=True, 
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    lastname = forms.CharField(required=False, 
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    choices = (('1', 'Male'),('2','Female'),)
    gender = forms.ChoiceField(required=True, widget=forms.RadioSelect, choices=choices)
    mail_id = forms.EmailField(required=True, 
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    dob = forms.DateField(label="DOB(mm/dd/yyy)", required=False, 
                          widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_no = forms.CharField(required=False, 
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
            
            
    def clean_mail_id(self):
        mail = self.cleaned_data.get('mail_id')
        if Users.objects.filter(mail_id__icontains=mail).exists():
            raise forms.ValidationError("Email id is already registered")
        return mail
        
            
    def clean_username(self):
        name = self.cleaned_data.get('username')
        if Users.objects.filter(username__iexact=name).exists():
            raise forms.ValidationError("This Username is Already used Choose another one")
        return name
    
       
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Password need to be more than 8 Characters")
        return password
 

from django.contrib.auth.models import User       
      
class ChangePasswordForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput())
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Old password",
        required=True)

    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="New password",
        required=True)
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm new password",
        required=True)

    class Meta:
        model = User
        fields = ['id', 'old_password', 'new_password', 'confirm_password']

    def clean(self):
        super(ChangePasswordForm, self).clean()
        old_password = self.cleaned_data.get('old_password')
        new_password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')
        id = self.cleaned_data.get('id')
        user = User.objects.get(pk=id)
        if not user.check_password(old_password):
            self._errors['old_password'] = self.error_class([
                'Old password don\'t match'])
        if new_password and new_password != confirm_password:
            self._errors['new_password'] = self.error_class([
                'Passwords don\'t match'])
        return self.cleaned_data


class Picture_change_Form(forms.ModelForm):
    class Meta:
        model = Users
        fields = ["profile_pic"]


class Status_change_form(forms.ModelForm):
    class Meta:
        model = Users
        fields = ["status"]
        
class Edit_Form(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['firstname', 'lastname', 'mail_id', 'username', 'dob', 'phone_no',
                  ]
        
        