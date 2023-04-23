from django.db.models.signals import post_save, post_delete  # сигнализирование
from django.dispatch import receiver  # декорирование о сигнализировании
from .models import Profile
from django.contrib.auth.models import User


# Сигнализирование о действиях пользователей
@receiver(post_save, sender=User)
def profile_create(sender, instance, created, **kwargs):
    print('Профиль сохранен!')
    if created:  # если создаем пользователя то
        user = instance  # в эту переменную сохраняем данные пользователя
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )  # create - создать экземпляр модели


@receiver(post_save, sender=Profile)
def update_user(sender, instance, created, **kwargs):  # редактирование профиля
    profile = instance
    user = profile.user

    if created is False:  # если пользователя не создаем, а обновляем
        user.first_name = profile.name  # перезаписываем в базе данных
        user.username = profile.username
        user.email = profile.email
        user.save()


@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    user = instance.user  # сохраняем в переменную пользователя которого будем удалять
    user.delete()  # delete- удаляет определенный объект

# Можно вызовом, но мы сделали с помощью декоратора
# post_save.connect(profile_create, sender=Profile)
# post_delete.connect(delete_user, sender=Profile)
