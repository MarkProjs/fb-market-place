from .models import Message
from django import forms


class SendMessage(forms.ModelForm):
    receiver = forms.CharField(required=True)
    body = forms.CharField(max_length=1000, required=True)

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'body']
