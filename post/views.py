from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import SingleObjectMixin
from .form import CommentForm
from .models import Post
from django.views import View
# Create your views here.
class PostView(ListView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    
    
class CommentGet(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm
        return context 
    
class CommentPost(SingleObjectMixin, FormView):
    model = Post
    form_class = CommentForm
    template_name = 'post_detail.html'
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        post = self.get_object()
        return reverse("post_detail", kwargs={"pk": post.pk})


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ('title', 'body')
    template_name = 'post_edit.html'
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user #type: ignore
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post')
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user #type: ignore
    
class PostDetailView(LoginRequiredMixin, DetailView):
    
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view() 
        return view(request, *args, **kwargs)
    
       
    
class PostCreateView(LoginRequiredMixin ,CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ('title', 'body')
    context_object_name = 'post'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    