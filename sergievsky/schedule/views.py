import json
from django.shortcuts import render, get_object_or_404
from .models import Schedule
from .forms import ScheduleCreateForm
from .handlers import handler_docx
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DeleteView, UpdateView, FormView, DetailView


class ScheduleListView(ListView):
    model = Schedule
    context_object_name = 'schedules'
    queryset = Schedule.objects.all().filter(published=True).order_by('-pk')
    template_name = 'schedule/list.html'
    raise_exception = True


class ScheduleCreateView(FormView):
    form_class = ScheduleCreateForm
    fields = ['title', 'data', 'published']
    template_name = 'schedule/create.html'
    success_url = reverse_lazy('list_schedules')
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
    fields = ['title', 'data', 'published']
    template_name = 'schedule/update.html'
    raise_exception = True


class ScheduleDetailView(DetailView):
    model = Schedule
    template_name = 'schedule/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ScheduleDetailView, self).get_context_data(**kwargs)
        schedule = self.object
        data_dict = json.loads(schedule.data)
        lst = []
        for table_key, value_start in data_dict.items():
            title_table = value_start['title_table']
            for k, v in value_start['tables'].items():
                lst.append({title_table: v})
        schedule.data = lst
        return context


class ScheduleDeleteView(DeleteView):
    model = Schedule
    success_url = reverse_lazy('list_schedules')
    template_name = 'schedule/delete.html'
    raise_exception = True

    def post(self, request, *args, **kwargs):
        if 'Cancel' in request.POST:
            return HttpResponseRedirect(self.success_url)
        else:
            return super(ScheduleDeleteView, self).post(request, *args, **kwargs)
