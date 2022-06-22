from django.http import HttpResponseRedirect
from .models import Post
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, \
    CreateView, DeleteView, UpdateView


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    queryset = Post.objects.all().filter(published=True).order_by('-pk')
    paginate_by = 7
    template_name = 'post/list.html'


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'published']
    template_name = 'post/create.html'
    raise_exception = True


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'published']
    template_name = 'post/update.html'
    raise_exception = True


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/detail.html'


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('list_posts')
    template_name = 'post/delete.html'
    raise_exception = True

    def post(self, request, *args, **kwargs):
        if 'Cancel' in request.POST:
            return HttpResponseRedirect(self.success_url)
        else:
            return super(PostDeleteView, self).post(request, *args, **kwargs)
