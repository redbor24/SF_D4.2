# импортируем библиотеку для работы с путями urls
from django.urls import path
# импортируем наше представление
from .views import PostListView, PostDetailedView, PostCreateView, PostUpdateView, PostDeleteView  #, PostSearchView

urlpatterns = [
    # поиск постов
    # path('search/', PostSearchView.as_view(), name='post_search'),
    # список постов
    path('', PostListView.as_view(), name='post_list'),
    # детали поста
    path('<int:pk>/', PostDetailedView.as_view(), name='post_details'),
    # создание поста
    path('create/', PostCreateView.as_view(), name='new_post_form'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='edit_post_form'), # Новый маршрут
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete_post_form'),
]