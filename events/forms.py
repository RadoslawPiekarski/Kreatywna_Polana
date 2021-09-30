from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, label="Login")
    password = forms.CharField(max_length=20, widget=forms.PasswordInput, label="Hasło")

# TODO add password widget for password file
# TODO add password2 field and validation password=password2
# TODO crypt password before sent


class CreateUserForm(forms.Form):
    username = forms.CharField(max_length=20, label="Login")
    password = forms.CharField(max_length=20, label="Hasło")
    firstname = forms.CharField(max_length=20, label="Imię")
    lastname = forms.CharField(max_length=50, label="Nazwisko")
    email = forms.EmailField(max_length=50, label="E-mail")
    phone_number = forms.CharField(max_length=20, label="Numer telefonu")

    # kid

    kid_name = forms.CharField(max_length=20, label="Imię uczestnika zajęć")
    birth_date = forms.DateField(label="Data urodzenia uczestnika zajęć (yyyy-mm-dd)")


# required=False - pole niewymagane
