from django import forms

class ContactForm(forms.Form):
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=50)
    email_address=forms.EmailField(max_length=100)
    contact_number=forms.CharField(max_length=10)
    message=forms.CharField(widget=forms.Textarea(attrs={'name':'body','rows':'4','cols':'10'}))
    