import datetime

from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

class PostModel(models.Model):
    title = models.CharField("Название поста", max_length=100, blank=False)
    discription = models.TextField("Описание", blank=False)
    date = models.DateField("Дата создания", default=datetime.date.today)
    top = models.BooleanField("Главная новость", blank=False)
    image = models.ImageField("Постер", upload_to='poster/')
    publick = models.BooleanField("Опубликован", default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
        # return reverse('post_detail', kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

class CountryModel(models.Model):
    name = models.CharField('Название страны', max_length=50, blank=False)
    image = models.ImageField('Изображение флага', upload_to='flag/', blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Старана'
        verbose_name_plural = 'Страны'

class ComandModel(models.Model):
        name = models.CharField('Название команды', max_length=100, blank=False)
        logo = models.ImageField('Логотип команды', upload_to='logo/', blank=False)
        country = models.ForeignKey(CountryModel, on_delete=models.SET_NULL, null=True,)

        def __str__(self):
            return self.name

        class Meta:
            verbose_name = 'Команда'
            verbose_name_plural = 'Команды'

class PlayerModel(models.Model):
    name = models.CharField('Полное имя игрока', max_length=100, blank=False)
    nickname = models.CharField('Ник игрока', max_length=50, blank=False)
    photo = models.ImageField('Фото игрока', upload_to='photo_player/')
    comand = models.ForeignKey(ComandModel, on_delete=models.CASCADE, verbose_name='Команда')
    country = models.ForeignKey(CountryModel, on_delete=models.SET_NULL, null=True, verbose_name='Страна')

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'

class TournamentModel(models.Model):
    name = models.CharField('Название турнира', max_length=150, blank=False)
    discription = models.TextField('Описанаие турнира', blank=False)
    comand = models.ManyToManyField(ComandModel, verbose_name='Команды участники турнира', related_name='comand_tournament')
    date = models.DateField('Дата начала турнира', blank=False)
    logo = models.ImageField('Логотип турнира', upload_to='logo_tournament/')
    prize_fond = models.SmallIntegerField('Призовой фонд', blank=False)
    active = models.BooleanField('Идёт в данный момент', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Турнир'
        verbose_name_plural = 'турниры'

class GameModel(models.Model):
    comand1 = models.ForeignKey(ComandModel, on_delete=models.CASCADE, verbose_name='Первая команда', related_name='one_comand')
    coefficient1 = models.DecimalField('Коэффициент на первую команду', max_digits=5, decimal_places=2, blank=False)
    coefficient2 = models.DecimalField('Коэффициент на вторую команду', max_digits=5, decimal_places=2, blank=False)
    comand2 = models.ForeignKey(ComandModel, on_delete=models.CASCADE, verbose_name='Вторая команда', related_name='two_comand')
    tournament = models.ForeignKey(TournamentModel, on_delete=models.CASCADE)
    active = models.BooleanField('Идёт в данный момент', default=False)
    last_game = models.BooleanField('Игра уже прошла', default=False)
    link = models.CharField('Сыылка на тотализатор', max_length=150, default=False)
    date = models.DateTimeField('Время начала игры', blank=False)

    def __str__(self):
        return f'{self.comand1}:{self.coefficient1}-{self.coefficient2}:{self.comand2}'

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

class ReitingModel(models.Model):
    comand = models.ForeignKey(ComandModel, on_delete=models.CASCADE)
    place_in_the_top = models.SmallIntegerField('Место в топе', blank=False, null=False)
    date = models.DateField('Дата рейтинга', auto_now_add=True, blank=False, null=False)
    form = models.SmallIntegerField('Форма команды', blank=False, null=False)
    victory = models.PositiveSmallIntegerField('колличество побед', blank=False, null=False)
    percent_victori = models.PositiveSmallIntegerField('Процент побед', blank=False, null=False)
    defeat = models.PositiveSmallIntegerField('Колиичество проигронных игр', blank=False, null=False)

    def __str__(self):
        return f'{self.comand}-{self.place_in_the_top}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'

class CommentModel(models.Model):
    # name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Commenter')
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField('Текст комментария', max_length=500, blank=False)
    date_create = models.DateTimeField('Время создание комментария', auto_now_add=True, blank=False)
    publick = models.BooleanField('Виден пользователям', default=True)

    def __str__(self):
        return f'{self.date_create}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

class ChanelModel(models.Model):
    name = models.CharField('Название канала', max_length=150)
    logo = models.ImageField('Логотип канала', upload_to='chanel/logo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Канал'
        verbose_name_plural = 'Каналы'

class VideoModel(models.Model):
    title = models.CharField('Название', max_length=150)
    discription = models.TextField('Описание', blank=True)
    tournament = models.ForeignKey(TournamentModel, on_delete=models.SET_NULL, null=True, verbose_name='Турнир', blank=True)
    game = models.ForeignKey(GameModel, on_delete=models.SET_NULL, null=True, verbose_name='Игра', blank=True)
    chanel = models.ForeignKey(ChanelModel, on_delete=models.SET_NULL, null=True, verbose_name='Канал')
    date = models.DateField(auto_now_add=True)
    live = models.BooleanField('Прямой эфир', default=False)
    link = models.CharField('Ссылка на видео', max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видосы'