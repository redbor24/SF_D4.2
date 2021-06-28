from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# создаем модель сообщения
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.CharField(max_length=100, blank=False)
    body = models.CharField(max_length=8000, blank=True)
    post_date = models.DateField()

    def __str__(self):
        return f'"{self.header}", автор: {self.author.username.title()}'

    # можно использовать этот метод для перехода на указанный в нём путь после успешного выполнения POST-метода,
    # а можно просто прописать во views.py success_url = reverse_lazy('<нужный путь>') и не грузить модель
    # фронтендовскими заморочками
    # def get_absolute_url(self):  # Тут мы создали новый метод
    #     # return reverse('post_details', args=[str(self.id)])
    #     return reverse('post_list') #, args=[str(self.id)])