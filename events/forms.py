from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, label="Login")
    password = forms.CharField(max_length=20, widget=forms.PasswordInput, label="Hasło")


class CreateUserForm(forms.Form):
    login = forms.CharField(max_length=20, label="Login")
    password = forms.CharField(max_length=20, label="Hasło")
    name = forms.CharField(max_length=20, label="Imię")
    surname = forms.CharField(max_length=50, label="Nazwisko")
    email = forms.EmailField(max_length=50, label="E-mail")
    phone_number = forms.CharField(max_length=20, label="Numer telefonu")

    # kid

    kid_name = forms.CharField(max_length=20, label="Imię uczestnika zajęć")
    birth_date = forms.DateField(label="Data urodzenia uczestnika zajęć (yyyy-mm-dd)")


# required=False - pole niewymagane
