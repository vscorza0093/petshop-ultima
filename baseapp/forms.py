from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    date = forms.DateTimeField()
    message = forms.CharField(widget=forms.Textarea)


class PetShowerForm(forms.Form):
    petName = forms.CharField()
    phone = forms.CharField()
    bookingDate = forms.DateTimeField()
    observations = forms.CharField()
