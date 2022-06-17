import uuid
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=99)
    title_image = models.ImageField(
        upload_to='post_image',
        blank=True
    )
    content = models.TextField()
    slug = models.SlugField(max_length=42, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('post_details', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = uuid.uuid4().hex
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post} - {self.name}'
