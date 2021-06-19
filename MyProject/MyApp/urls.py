# импортируем библиотеку для работы с путями urls
from django.urls import path
# импортируем наше представление
from .views import PostListView, PostDetailedView, PostCreateView #, PostSearchView

urlpatterns = [
    # поиск постов
    # path('search/', PostSearchView.as_view(), name='post_search'),
    # список постов
    path('', PostListView.as_view(), name='post_list'),
    # детали поста
    path('<int:pk>/', PostDetailedView.as_view(), name='post_details'),
    # создание поста
    path('<int:pk>/', PostCreateView.as_view(), name='post_create'),
]