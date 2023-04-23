from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import logout, login, authenticate  # для разлогинивания/залогинивание/проверка на авторизацию
from django.contrib.auth.models import User  # модель БД для авторизации
from django.core.exceptions import ObjectDoesNotExist  # если не будет пользователя
from django.contrib import messages  # для вывода пользователю уведомлений
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, SkillForm
from .utils import search_profiles


def login_user(request):  # авторизация пользователя
    if request.user.is_authenticated:  # если пользователь авторизирован
        return redirect('profiles')

    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:  # если пользователь не существует
            messages.error(request, 'Пользователя не существует')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Неверно введено имя пользователя или пароль')

    return render(request, 'users/login_register.html')


def logout_user(request):
    logout(request)
    messages.error(request, 'Вы вышли из аккаунта')
    return redirect('login')


def profiles(request):
    profile, search_query = search_profiles(request)  # распаковка кортежа
    context = {'profiles': profile, 'search_query': search_query}
    return render(request, 'users/index.html', context)


def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)  # Модель профиля по ключу

    top_skills = profile.skill_set.exclude(description__exact="")  # исключаем пустое поле description
    other_skills = profile.skill_set.filter(description='')  # если пустое запишем в other_skill

    context = {
        'profile': profile,
        'top_skills': top_skills,
        'other_skills': other_skills
    }
    return render(request, 'users/profile.html', context)


@login_required(login_url='login')
def user_account(request):  # Мой аккаунт
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    context = {
        'profile': profile,
        'skills': skills,
        'project': projects
    }
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def edit_account(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':  # если отправляем данные с формы
        form = ProfileForm(request.POST, request.FILES,
                           instance=profile)  # в переменную записываем данные,изображения,к определенному пользователю
        if form.is_valid():
            form.save()

            return redirect('account')

    context = {'form': form}
    return render(request, 'users/profile_form.html', context)


@login_required(login_url='login')
def create_skill(request):
    profile = request.user.profile
    form = SkillForm()

    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, 'Навык добавлен')
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/skill_form.html', context)


@login_required(login_url='login')
def update_skill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Навык обновлен')
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/skill_form.html', context)


@login_required(login_url='login')
def delete_skill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Навык был удален успешно')
        return redirect('account')
    context = {'object': skill}
    return render(request, 'users/delete.html', context)

