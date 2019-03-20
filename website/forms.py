from django import forms
from website.models import Album

class ContactForm(forms.Form):
        Nome = forms.CharField(required=True)
        Email  = forms.EmailField(required=True)
        Mensagem = forms.CharField(widget=forms.Textarea, required=True)


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = []

    zip = forms.FileField(required=False)
