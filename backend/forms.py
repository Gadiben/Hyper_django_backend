from django import forms

class ConnexionForm(forms.Form):
    pseudo = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    cleaned_data = None
    # password = forms.CharField(label="Mot de passe", max_length=10)