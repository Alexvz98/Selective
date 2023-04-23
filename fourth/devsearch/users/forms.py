from .models import Profile, Skill
from django.forms import ModelForm
from django import forms


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'  # все поля
        exclude = ['owner']  # исключаем поля

    def __init__(self, *args, **kwargs):  # для применения стилей к инпутам
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class ProfileForm(ModelForm):  # Форма редактирования аккаунта
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'short_info', 'bio',
                  'profile_image', 'whatsapp', 'instagram', 'vkontakte']

    def __init__(self, *args, **kwargs):  # для применения стилей к инпутам
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class ModalForm(forms.Form):
    name = forms.CharField(min_length=2, widget=forms.TextInput(attrs={'placeholder': "Ваше имя:"}))
    telephone = forms.CharField(min_length=10, widget=forms.TextInput(attrs={'placeholder': "Ваш номер телефона:"}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

