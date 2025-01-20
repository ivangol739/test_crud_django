from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label='Имя', initial='undefined', help_text='Введите свое имя')
    age = forms.IntegerField(label='Ваш возраст?', widget=forms.Textarea, initial=18, help_text='Введите свой возраст')