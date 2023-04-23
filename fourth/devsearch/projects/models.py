from django.db import models
from users.models import Profile


class Project(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    featured_image = models.ImageField(null=True, blank=True, upload_to='projects/%Y/%m/%d/', default='default.jpg',
                                       verbose_name='Изображение')
    demo_link = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Ссылка(по необходимости')
    source_link = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Ссылка(по необходимости)')
    tags = models.ManyToManyField('Tag', blank=True, verbose_name='Тэги')

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название тэга')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comments(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    text = models.TextField(verbose_name='Отзыв')
    date = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.name
