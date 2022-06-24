from django import forms
from .models import Schedule


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['title', 'published']
        exclude = ['data', 'slug', ]

    document = forms.FileField()
