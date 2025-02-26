from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'password', 'age', 'birth_date', 'phone']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'first_name': 'Primeiro nome',
            'last_name': 'Ultimo nome',
            'email': 'Email',
            'password': 'Senha',
            'age': 'Idade',
            'birth_date': 'Data de Nascimento',
            'phone': 'Celular',
        }