from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Nom', max_length=100)
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Téléphone', max_length=20, required=False)
    message = forms.CharField(label='Message', widget=forms.Textarea)
