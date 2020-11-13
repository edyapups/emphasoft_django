from django.shortcuts import render, redirect, Http404
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.decorators import login_required
from . import forms
from .models import User


def login(request):
    return render(request, 'emphasoft_app/login.html')


@login_required()
def me(request):
    return redirect('emphasoft_app:user', user_id=request.user.id)


@login_required()
def index(request):
    return render(request, 'emphasoft_app/index.html', context={
        'users': User.objects.all().order_by('-last_login'),
    })


@login_required()
def user_page(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        return render(request, 'emphasoft_app/user.html', context={
            'user': user,
        })
    except User.DoesNotExist:
        raise Http404


@login_required()
@transaction.atomic()
def edit_user(request):
    if request.method == "POST":
        user_form = forms.UserForm(request.POST, instance=request.user)
        profile_form = forms.ProfileForm(request.POST, instance=request.user.profile, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Ваш профиль был успешно обновлен!')
            return redirect('emphasoft_app:user', user_id=request.user.id)
        else:
            messages.error(request, 'У вас какие-то ошибки, кажется.')
    else:
        user_form = forms.UserForm(instance=request.user)
        profile_form = forms.ProfileForm(instance=request.user.profile)
    return render(request, 'emphasoft_app/edit_user.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
