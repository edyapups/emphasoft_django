from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def login(request):
    return render(request, 'emphasoft_app/login.html')


@login_required()
def index(request):
    pass

# Create your views here.
