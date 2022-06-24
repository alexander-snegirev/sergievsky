from django.urls import path
from .views import ScheduleListView, ScheduleDetailView, ScheduleUpdateView, ScheduleDeleteView, ScheduleCreateView, schedule_detail


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
    path(
        '<slug:slug>/update',
        ScheduleUpdateView.as_view(),
        name='schedule_update'
    ),
    # path(
    #     '<slug:slug>',
    #     ScheduleDetailView.as_view(),
    #     name='schedule_details'
    # ),
    path(
        '<slug:slug>',
        schedule_detail,
        name='schedule_details'
    ),
    path(
        '<slug:slug>/delete',
        ScheduleDeleteView.as_view(),
        name='schedule_delete'
    )
]
