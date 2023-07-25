from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class PetShowerForm(forms.Form):
    petName = forms.CharField()
    phone = forms.CharField()
    bookingDate = forms.DateField()
    observations = forms.CharField()
