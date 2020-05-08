from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.generic import ListView, DetailView
from .models import PostModel

class Post:
    """Вывод не топовых новостей"""
    def get_post(self):
        return PostModel.objects.filter(top=False, publick=True)[:6]


class PostList(ListView, Post):
    model = PostModel
    queryset = PostModel.objects.filter(top=True, publick=True)[:3]

class PostDetail(DetailView):
    model = PostModel