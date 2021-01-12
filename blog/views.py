from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from .models import AddBlog


# Create your views here.


class AddBlogView(ListView):
    model = AddBlog
    ordering = ['-id']
    template_name = 'bloghome.html'


class CreateBlogView(CreateView):
    model = AddBlog
    template_name = 'addblog.html'
    fields = '__all__'
    success_url = reverse_lazy('bloghome')


class DeleteBlogView(DeleteView):
    model = AddBlog
    template_name = 'deleteblog.html'
    success_url = reverse_lazy('bloghome')
