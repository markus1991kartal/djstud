from django import forms

class CommentForm(forms.Form):
    auth = forms.CharField()
    text = forms.CharField()