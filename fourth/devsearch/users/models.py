from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Логин')
    name = models.CharField(max_length=200, null=True, blank=True,verbose_name='Имя пользователя')
    email = models.EmailField(max_length=200, null=True, blank=True)  # EmailField - валидация от джанго
    username = models.CharField(max_length=200, blank=True, null=True, verbose_name='Никнейм пользователя')
    short_info = models.CharField(max_length=200, blank=True, null=True,verbose_name='Краткая информация о пользователе')  # профессия
    bio = models.TextField(blank=True, null=True, verbose_name='Полная информация')  # инфо о себе
    profile_image = models.ImageField(blank=True, null=True, upload_to='profiles/',
                                      default='profiles/user-default.png',verbose_name='Фото')
    whatsapp = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    vkontakte = models.CharField(max_length=200, null=True, blank=True)
    telegram = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.username}'


class Skill(models.Model):  # скилы(навыки) пользователя
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)  # связь с профилем
    name = models.CharField(max_length=200, null=True, blank=True)  # имя навыка
    description = models.TextField(null=True, blank=True)  # описание навыка
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

