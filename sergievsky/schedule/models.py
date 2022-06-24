import uuid
from django.db import models
from django.urls import reverse


class Schedule(models.Model):
    title = models.CharField(max_length=99)
    data = models.JSONField()
    slug = models.SlugField(max_length=42, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('schedule_details', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = uuid.uuid4().hex
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'
