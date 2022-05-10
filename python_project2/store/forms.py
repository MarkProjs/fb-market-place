from django import forms
from .models import Product, Comment, rating_choices


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'rating')

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }




