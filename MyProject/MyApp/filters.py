# импортируем filterset
from django_filters import FilterSet
# импортируем модель Post
from .models import Post


# создаём фильтр
class PostFilterSet(FilterSet):
    class Meta:
        model = Post
        fields = {
            # по автору
            'author': ['exact'],
            # по названию
            'header': ['icontains'],
            # позже даты создания
            'post_date': ['gt'],
        }
