from django.shortcuts import render, redirect
from .models import Project, Tag, Comments
from .forms import ProjectForm, CommentForm  # импорт формы для создания проектов
from django.contrib.auth.decorators import \
    login_required  # декоратор для отключения функций не зарегестрированным пользователям
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages


def projects(request):
    pr = Project.objects.all()  # все данные из бд project

    page = request.GET.get('page')  # метод пагинации
    results = 3  # кол-во выводимых элементов
    paginator = Paginator(pr, results)

    try:
        pr = paginator.page(page)
    except PageNotAnInteger:  # если кол-во объектов <= results, то выведем все на одну страницу
        page = 1
        pr = paginator.page(page)  # вывод на одной странице
    except EmptyPage:  # если страница пустая
        page = paginator.num_pages  #
        pr = paginator.page(page)

    left_index = int(page) - 4
    if left_index < 1:
        left_index = 1

    right_index = int(page) + 5

    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    context = {"projects": pr,
               'paginator': paginator,
               'custom_range': custom_range

               }
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        review = form.save(commit=False)
        review.save()
        messages.success(request, 'Данные отправлены успешно')
        return redirect('project', pk=project_obj.id)

    return render(request, 'projects/single-project.html', {'project': project_obj, 'form': form})


@login_required(login_url='login')
def create_project(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':  # при записи данных в БД
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():  # проверка на валидацию встроенная django
            project = form.save(commit=False)
            project.owner = profile
            form.save()
            return redirect('account')  # если данные записанны , перенаправит на страницу проектов

    context = {'form': form}
    return render(request, 'projects/form-template.html', context)


@login_required(login_url='login')
def update_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        new_tags = request.POST.get('tags').replace(',', ' ').split()
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()
            for tag in new_tags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('account')

    context = {'form': form, 'project': project}
    return render(request, 'projects/form-template.html', context)


@login_required(login_url='login')
def delete_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    context = {'object': project}
    return render(request, 'projects/delete.html', context)
