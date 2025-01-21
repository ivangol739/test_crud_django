from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from .forms import UserForm
from .models import Person

# def index(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         age = request.POST.get("age")
#         return HttpResponse(f"<h2>Привет, {name}, твой возрас: {age}</h2>")
#     else:
#         userform = UserForm()
#         return render(request, "crud/index.html", {"form": userform})


# def index(request):
#     if request.method == "POST":
#         userform = UserForm(request.POST)
#         if userform.is_valid():
#             name = userform.cleaned_data['name']
#             return HttpResponse(f'<h2>Hello, {name}</h2>')
#         else:
#             return HttpResponse('Invalid data')
#     else:
#         userform = UserForm()
#         return render(request, 'crud/index.html', {'form': userform})


# def index(request):
#     userform = UserForm()
#     if request.method == 'POST':
#         userform = UserForm(request.POST)
#         if userform.is_valid():
#             name = userform.cleaned_data['name']
#             return HttpResponse(f'<h2>Hello, {name}</h2>')
#     return render(request, 'crud/index.html', {"form": userform})


# Получение данных из БД
def index(request):
    people = Person.objects.all()
    return render(request, 'crud/index.html', {'people': people})


# Сохранение данных в БД
def create(request):
    if request.method == 'POST':
        person = Person()
        person.name = request.POST.get('name')
        person.age = request.POST.get('age')
        person.save()
    return HttpResponseRedirect('/')