from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Post
# Create your views here.
class PostView(ListView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    
class PostCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ('title', 'body')
    context_object_name = 'post'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'body')
    template_name = 'post_edit.html'
    
class PostDeleteView(DeleteView):
    model = Post
    template_engine = 'post_delete.html'
    success_url = reverse_lazy('post')
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'