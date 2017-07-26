from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django import forms


class RegisterForm(UserCreationForm):

    password1 = forms.CharField(
        label="Parolanız",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Parolanızı Doğrulayın",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        strip=False,
    )
    class Meta:
        model = User
        fields = ('email','birth_date', 'student_number', 'faculty', 'department', 'grade')
        labels = {
            'email':'Email Adresiniz',
            'birth_date': 'Doğum Tarihi',
            'student_number':'Öğrenci Numarası',
            'faculty':'Fakülte',
            'department':'Bölüm',
            'grade':'Öğrenim Türü'
        }
        widgets = {
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'birth_date': forms.SelectDateWidget,
            'student_number': forms.TextInput(attrs={'class':'form-control'}),
            'faculty': forms.TextInput(attrs={'class':'form-control'}),
            'department': forms.TextInput(attrs={'class':'form-control'}),
            'grade': forms.Select(attrs={'class':'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'password2': forms.TextInput(attrs={'class': 'form-control'}),

        }
class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if not username or not password:
            return self.cleaned_data

        user = authenticate(username=username,
                            password=password)

        if user:
            self.user = user
        else:
            raise ValidationError("Yanlış kullanıcı adı veya şifre!")

        return self.cleaned_data