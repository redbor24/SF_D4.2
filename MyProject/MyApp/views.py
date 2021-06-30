from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Post
from django.urls import reverse_lazy  # импортируем новые методы
from .filters import PostFilterSet  # импортируем наш фильтр
from django.contrib.auth.mixins import LoginRequiredMixin


class FilteredPostListView(ListView):
    model = Post

    # зададим шаблон странички
    # если не задать, то django автоматически выведет это имя из названия модели
    # и получится newspaper/post_list.html, которая всё-равно будет находится в папке templates
    template_name = 'post_list.html'

    # также, можно указать название шаблона в поле context_object_name,
    # либо не указывать, тогда newspaper/post_list.html будет выбран по умолчанию, как шаблон
    context_object_name = 'post_list'

    # установим постраничный вывод на каждую новость через paginator
    # paginate_by = 10

    fields = ('author', 'header', 'body', 'post_date')

    # добавим ссылку на форму:
    # form_class = PostForm

    filterset_class = None  # переменная в последующем будет включать в себя класс фильтра

    # пишем метод, который принимает на вход отфильтрованные объекты
    def get_context_data(self, **kwargs):
        # распаковываем self = Posts
        context = super().get_context_data(**kwargs)
        context['post_search'] = self.filterset  # объявляем для шаблона способ обращения к отфильтрованному queryset
        # context['categories'] = PostCategory.objects.all()
        # context['post_form'] = PostForm()
        # общее количество элементов
        context['all_news_count'] = Post.objects.all().count()
        # количество элементов после применения фильтра
        context['posts_found'] = self.get_queryset().count()
        return context

    # сортируем все объекты модели Post по параметру даты создания в обратном порядке:
    def get_queryset(self):
        #  Получаем queryset
        queryset = super().get_queryset().order_by('post_date', 'id')
        #  Переопределяем queryset через filterset, который пока None, но будет объявлен потом при наследовании
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        # Возвращаем отсортированный queryset
        return self.filterset.qs.all()


#  наследуемся от FilteredListView и определяем FilterSet и пагинацию
class PostListView(FilteredPostListView):
    filterset_class = PostFilterSet
    paginate_by = 10


# пост детально
class PostDetailedView(DetailView):
    model = Post
    template_name = 'MyApp/post_details.html'
    queryset = Post.objects.all()


# создание поста
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    context_object_name = 'new_post_form'
    template_name = 'MyApp/post_create.html'
    fields = ('author', 'header', 'body', 'post_date')
    success_url = reverse_lazy('post_list')


# редактирование поста
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    context_object_name = 'edit_post_form'
    template_name = 'MyApp/post_edit.html'
    fields = ('header', 'body')
    success_url = reverse_lazy(viewname='post_list')


# удаление поста
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    context_object_name = 'delete_post_form'
    template_name = 'MyApp/post_delete.html'
    fields = ('header', 'post_date')
    success_url = reverse_lazy('post_list')


