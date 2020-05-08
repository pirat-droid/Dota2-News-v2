from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.generic import ListView, DetailView
from .models import PostModel, GameModel, VideoModel

class Post:
    """Вывод не топовых новостей"""
    def get_post(self):
        return PostModel.objects.filter(top=False, publick=True)[:6]

class Game:
    """"Список текущих игр"""
    def get_game(self):
        return GameModel.objects.filter(last_game=False)

class LiveStream:
    """Прямая трансляция"""
    def get_livestream(self):
        return VideoModel.objects.filter(live=True)[:1]


class PostList(ListView, Post, Game, LiveStream):
    model = PostModel
    queryset = PostModel.objects.filter(top=True, publick=True)[:3]

class PostDetail(DetailView, Game, LiveStream):
    model = PostModel