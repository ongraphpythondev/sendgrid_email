from django import forms


class EmailForm(forms.Form):
    _from = forms.EmailField()
    to = forms.EmailField()
    subject = forms.CharField(max_length=160)
    body = forms.CharField(widget=forms.Textarea)

