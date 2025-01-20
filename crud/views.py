from django.shortcuts import render
from .forms import UserForm


def index(request):
    userform = UserForm()
    return render(request, 'crud/index.html', {'form': userform})
