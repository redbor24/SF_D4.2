from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from .models import Post

# импортируем класс, позволяющий удобно осуществлять постраничный вывод
from django.core.paginator import Paginator

# импортируем созданную нами форму
from .forms import PostForm  # , PostSearchForm  # т.к. мы создали именно class PostForm(ModelForm)

# импортируем наш фильтр
from .filters import PostFilterSet


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

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     return super().get(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        # берём значения для нового товара из POST-запроса отправленного на сервер
        author = request.POST['author']
        header = request.POST['header']
        body = request.POST['body']
        post_date = request.POST['post_date']

        Post(author=User.objects.get(username=author), header=header, body=body, post_date=post_date).save()
        return super().get(request, *args, **kwargs)  # отправляем пользователя обратно на GET-запрос.


# пост детально
class PostDetailedView(DetailView):
    template_name = 'MyApp/post_details.html'
    queryset = Post.objects.all()


# создание поста
class PostCreateView(CreateView):
    context_object_name = 'new_post_form'
    template_name = 'MyApp/post_create.html'
    form_class = PostForm


# поиск постов
# class PostSearchView(CreateView):
#     context_object_name = 'post_search'
#     template_name = 'MyApp/post_search.html'
#     # form_class = PostSearchForm
#
