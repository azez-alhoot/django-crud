from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from .models import Post
# Create your views here.

class BlogListView(ListView):
    template_name = 'blogs.html'
    model = Post

class BlogDetailView(DetailView):
    template_name = 'blogs-detail.html'
    model = Post

class BlogCreateView(CreateView):
    template_name = 'create-post.html'
    model = Post
    fields = ['title','author','body']

class BlogUpdateView(UpdateView):
    template_name = 'update-post.html'
    model = Post
    fields = ['title','author','body']

class BlogDeleteView(DeleteView):
    template_name = 'delete-post.html'
    model = Post
    success_url = reverse_lazy('blogs')