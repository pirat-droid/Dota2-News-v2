from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from .models import PostModel, ReitingModel, CountryModel, ComandModel, PlayerModel, TournamentModel, GameModel, CommentModel

@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'get_image', 'top', 'publick')
    list_filter = ('date', 'top')
    list_editable = ('top', 'publick')
    search_fields = ('title',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="82" height="50">')

    get_image.short_description = "Постер"

@admin.register(CountryModel)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_image')
    search_fields = ('name',)


    def get_image(self, obj):
        return  mark_safe(f'<img src={obj.image.url} width="64" height="50">')

    get_image.short_description = 'Флаг'

@admin.register(ComandModel)
class ComandAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'get_image')
    list_filter = ('country',)
    search_fields = ('name',)

    def get_image(self, obj):
        return  mark_safe(f'<img src={obj.logo.url} width="50" height="50">')

    get_image.short_description = 'Логотип'

@admin.register(PlayerModel)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'nickname', 'get_image', 'comand', 'country')
    list_filter = ('comand', 'country')
    search_fields = ('name', 'nickname')

    def get_image(self, obj):
        return mark_safe(f'<img  src={obj.photo.url} width="62" height="82">')

    get_image.short_description = 'Фото'

@admin.register(TournamentModel)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_image', 'date', 'prize_fond', 'active')
    list_filter = ('date', 'active')
    list_editable = ('active',)
    search_fields = ('name',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.logo.url} width"82", height="60">')

    get_image.short_description = 'Логотип турнира'

@admin.register(GameModel)
class GameAdmin(admin.ModelAdmin):
    list_display = ('comand1', 'coefficient1', 'coefficient2', 'comand2', 'tournament', 'active', 'last_game', 'date')
    list_filter = ('tournament', 'date', 'active', 'last_game')
    list_editable = ('active', 'last_game')
    search_fields = ('comand1', 'comand2')

@admin.register(ReitingModel)
class ReitingAdmin(admin.ModelAdmin):
    list_display = ('comand', 'place_in_the_top', 'form', 'victory', 'percent_victori', 'defeat', 'date')
    list_filter = ('date',)
    search_fields = ('comand',)

@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'date_create', 'publick')
    list_filter = ('date_create',)
    search_fields = ('name', 'post')
