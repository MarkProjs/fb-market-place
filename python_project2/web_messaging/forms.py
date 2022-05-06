from .models import Message
from django import forms


class SendMessage(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'message']
