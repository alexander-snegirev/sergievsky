import json

from django.shortcuts import render

from .models import Schedule
from .forms import ScheduleForm
from .handlers import handler_docx
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import (DetailView, ListView, DeleteView, UpdateView, FormView)


class ScheduleListView(ListView):
    model = Schedule
    context_object_name = 'schedules'
    queryset = Schedule.objects.all().filter(published=True).order_by('-pk')
    template_name = 'schedule/list.html'
    raise_exception = True


class ScheduleCreateView(FormView):
    form_class = ScheduleForm
    fields = ['title', 'data', 'published']
    template_name = 'schedule/create.html'
    raise_exception = True

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        data = handler_docx.get_data(request.FILES['document'])
        if form.is_valid():
            title = form.cleaned_data['title']
            published = form.cleaned_data['published']
            schedule_obj = Schedule.objects.create(title=title, data=data, published=published)
            schedule_obj.save()
        return HttpResponseRedirect(self.success_url)


class ScheduleUpdateView(UpdateView):
    model = Schedule
    fields = ['title', 'content', 'published']
    template_name = 'schedule/update.html'
    raise_exception = True


class ScheduleDetailView(DetailView):
    model = Schedule
    template_name = 'schedule/detail.html'


def schedule_detail(request, slug):
    schedule = Schedule.objects.get(slug=slug)
    data_dict = json.loads(schedule.data)
    lst = []
    for table_key, value_start in data_dict.items():
        title_table = value_start['title_table']
        for k, v in value_start['tables'].items():
            lst.append({title_table: v})
    print(len(lst))
    return render(request, 'schedule/detail.html', context={'schedule': lst})


class ScheduleDeleteView(DeleteView):
    model = Schedule
    success_url = reverse_lazy('list_posts')
    template_name = 'schedule/delete.html'
    raise_exception = True

    def post(self, request, *args, **kwargs):
        if 'Cancel' in request.POST:
            return HttpResponseRedirect(self.success_url)
        else:
            return super(ScheduleDeleteView, self).post(request, *args, **kwargs)
