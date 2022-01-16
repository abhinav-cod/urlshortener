from django import forms
from .models import tinyurls

class tinyurlsform(forms.ModelForm):
    original_url=forms.URLField(widget=forms.URLInput(attrs={"class":"form-control form-control-lg", "placeholder":"Your original URL"}))

    class Meta:
        model=tinyurls

        fields = ('original_url', )
