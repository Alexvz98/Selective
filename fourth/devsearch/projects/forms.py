from django.forms import ModelForm
from .models import Project,Comments
from django import forms


class ProjectForm(ModelForm):  # наследуемся от встроенного модуля ModelForm
    class Meta:
        model = Project  # обязательные переменные
        fields = ['title', 'description', 'featured_image', 'demo_link', 'source_link',
                  'tags']  # Вывод конкретных полей

        widgets = {
            'tags': forms.CheckboxSelectMultiple()  # выбор тегов чек-бокс
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
