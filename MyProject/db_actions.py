#from db_actions import init
# >>> init()
# a = Author.objects.get(author_name='author2')
# a.update_rating()
# Author.objects.get(author_name='author2').update_rating()

from datetime import datetime
from django.contrib.auth.models import User
from MyApp.models import Post


def init():
    print(f'DB initialization started...')

    print(f' Очистка объектов...')
    User.objects.all().delete()
    print(f'  Users = {User.objects.count()}')
    Post.objects.all().delete()
    print(f'  Posts = {Post.objects.count()}')
    print(f' Очистка объектов завершена')

    print(f' Ввод новых данных...')
    print(f'  Создание пользователей...')
    User(username="user1").save()
    User(username="user2").save()
    print(f'   пользователей: {User.objects.count()}')
    print(f'  Пользователи созданы')

    print(f'  Создание постов и новостей...')
    a = User.objects.get(username='user1')
    Post(author=a, header='NewsHeader1',
             post_date=datetime.strptime('2021-06-01 10:30', '%Y-%m-%d %H:%M'),
             body="""Слово1 слово2 плохое_слово1 плохое_слово2
плохое_слово3 слово3
1234567890
1234567890
1234567890
1234567890
1234567890
""").save()

    Post(author=a, header='NewsHeader2',
             post_date=datetime.strptime('2021-06-06 04:21', '%Y-%m-%d %H:%M'),
             body="""Слово1 слово2 плохое_слово1 плохое_слово2
    плохое_слово3 плохое_слово4""").save()

    a = User.objects.get(username='user2')
    for i in range(1, 31):
        Post(
            author=a,
            header=f'NewsHeader{i + 10}',
            post_date=datetime.strptime(f'2021-06-{i:02d}', '%Y-%m-%d'),
            body=f'news_body{i + 10}'
        ).save()

    print(f'   постов: {Post.objects.all().count()}')
    print(f'  Посты созданы')
    exit()