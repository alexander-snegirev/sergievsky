from django.urls import path
from .views import ScheduleListView, ScheduleUpdateView, ScheduleDeleteView, ScheduleCreateView, ScheduleDetailView


urlpatterns = [
    path(
        'list',
        ScheduleListView.as_view(),
        name='list_schedules'
    ),
    path(
        'create',
        ScheduleCreateView.as_view(),
        name='schedule_create'
    ),
    # path(
    #     '<slug:slug>/update',
    #     ScheduleUpdateView.as_view(),
    #     name='schedule_update'
    # ),
    path(
        '<slug:slug>',
        ScheduleDetailView.as_view(),
        name='schedule_details'
    ),
    path(
        '<slug:slug>/delete',
        ScheduleDeleteView.as_view(),
        name='schedule_delete'
    )
]
