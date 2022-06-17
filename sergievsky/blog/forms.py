from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.CharField(attrs={
        'placeholder': 'Enter your name'
    }))
    content = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'W your content'
    }))

    class Meta:
        model = Comment
        fields = ('name', 'content', )
