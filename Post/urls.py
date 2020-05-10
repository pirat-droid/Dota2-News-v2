from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('post/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('<int:pk>', views.AddComment.as_view(), name='add_comment'),
    path('all-news/', views.AllNews.as_view(), name='all_news'),
    path('all-video/', views.AllVideo.as_view(), name='all_video'),
    path('all-game/', views.AllGame.as_view(), name='all_game'),
    path('reiting/', views.Reiting.as_view(), name='reiting'),
]