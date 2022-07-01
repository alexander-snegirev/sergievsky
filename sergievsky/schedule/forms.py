from django.forms import ModelForm, CharField, FileField, Textarea, CheckboxInput
from .models import Schedule


class ScheduleCreateForm(ModelForm):
    class Meta:
        model = Schedule
        fields = ['title', 'published']
        exclude = ['data', 'slug']
        widgets = {
            'title': Textarea(attrs={'class': 'form-control', 'rows': 1, 'style': 'resize: none;'}),
            'published': CheckboxInput(attrs={'class': 'form-check-input'})
        }

    document = FileField()
    document.widget.attrs.update({'class': 'form-control', 'id': 'formFile'})


class ScheduleUpdateForm(ModelForm):
    class Meta:
        model = Schedule
        fields = ['title', 'published']

    document = FileField()
