from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','password','birth_date', 'student_number', 'faculty', 'department', 'grade')
        labels = ('Email','Parola','Doğum Tarihi', 'Öğrenci Numarası', 'Fakülte', 'Bölüm', 'Öğrenim Türüdü')

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