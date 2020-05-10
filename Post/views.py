from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.generic import ListView, DetailView, CreateView, View
from .models import PostModel, GameModel, VideoModel, ReitingModel
from .forms import CommentForm

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

class AddComment(View):
    """Добавление комментария"""
    def post(self, request, pk, ):
        form = CommentForm(request.POST)
        number = PostModel.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.post = number
            form.author = request.user
            form.save()
        return redirect('post/'+str(pk))

class AllNews(ListView, Game, LiveStream):
    """Все новости"""
    model = PostModel
    queryset = PostModel.objects.filter(publick=True)
    template_name = 'Post/allpost_list.html'
    paginate_by = 6

class AllVideo(ListView, Game, LiveStream):
    """Все видео"""
    model = VideoModel
    queryset = VideoModel.objects.filter(live=False)
    template_name = 'Post/allvideo_list.html'
    paginate_by = 6

class AllGame(ListView, Game, LiveStream):
    """Все игры"""
    model = GameModel
    queryset = GameModel.objects.all()
    template_name = 'Post/allgame_list.html'
    paginate_by = 6

class Reiting(ListView, Game, LiveStream):
    """Рейтинг команд"""
    model = ReitingModel
    queryset = ReitingModel.objects.all()
    template_name = 'Post/reiting_list.html'
