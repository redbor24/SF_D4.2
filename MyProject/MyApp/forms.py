from django.forms import ModelForm, BooleanField
from .models import Post


# создаём модельную форму
class PostForm(ModelForm):
    # check_box = BooleanField(label='Галочка')  # добавляем галочку, или же true-false поле

    class Meta:
        model = Post  # это модель, по которой будет строиться форма

        # поля, которые будут выводиться на страничке
        fields = ['author', 'header', 'body', 'post_date']


# форма поиска
# class PostSearchForm(ModelForm):
#     class Meta:
#         model = Post  # это модель, по которой будет строиться форма
#
#         # поля, которые будут выводиться на страничке
#         fields = ['header', 'body', 'post_date']
