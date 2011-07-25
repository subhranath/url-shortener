from django import forms

class URLShortifyForm(forms.Form):
    """Form to shorten an URL.
    """
    url = forms.URLField(max_length=2000, verify_exists=False)
    