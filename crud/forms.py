from django.forms import Form, CharField, IntegerField

from crud.models import Person


class PersonForm(Form):
    name = CharField(label='Введите имя')
    age = IntegerField(label='Введите возраст')

    class Meta:
        model = Person
        fields = ['name', 'age']