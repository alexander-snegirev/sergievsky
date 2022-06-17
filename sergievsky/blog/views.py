from django.http import HttpResponseRedirect
from .forms import CommentForm
from .models import Post, Comment
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
    fields = ['__all__']
    # template_name = 'post/create.html'
    raise_exception = True


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'title_image', 'published']
    # template_name = 'post/update.html'
    raise_exception = True


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/detail.html'
    form = CommentForm

    def get_context_data(self, **kwargs):
        ctx = super(PostDetailView, self).get_context_data(**kwargs)
        ctx['comments'] = Comment.objects.all()
        ctx['form'] = self.form
        return ctx

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        print(self.get_object())
        print(f'[args] {args}', f'[kwargs] {kwargs}')
        if comment_form.is_valid():
            print('[COMMENT POST IS VALID]', self.get_object())
            new_comment = comment_form.save(commit=False)
            new_comment.save()
            return HttpResponseRedirect('list_posts')
        print('PASS')
        return HttpResponseRedirect('list_posts')


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


class CommentListView(ListView):
    model = Comment
    queryset = Comment.objects.all()
    context_object_name = 'comments'
    template_name = 'comment/list.html'


class CommentCreateView(CreateView):
    model = Comment
    fields = ['name', 'context']
    template_name = 'comment/create.html'
    raise_exception = True


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'comment/delete.html'
    success_url = reverse_lazy('list_posts')
    raise_exception = True
