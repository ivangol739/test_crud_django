from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm


# def index(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         age = request.POST.get("age")
#         return HttpResponse(f"<h2>Привет, {name}, твой возрас: {age}</h2>")
#     else:
#         userform = UserForm()
#         return render(request, "crud/index.html", {"form": userform})


def index(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data['name']
            return HttpResponse(f'<h2>Hello, {name}</h2>')
        else:
            return HttpResponse('Invalid data')
    else:
        userform = UserForm()
        return render(request, 'crud/index.html', {'form': userform})
