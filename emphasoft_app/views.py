from django.shortcuts import render, redirect, Http404
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.decorators import login_required
from . import forms
from .models import User


def login(request):
    """
    Renders an authentication page.

    :param request: Request object.
    """
    return render(request, 'emphasoft_app/login.html')


@login_required()
def me(request):
    """
    Redirects to the authenticated user page.

    :param request: Request object.
    """
    return redirect('emphasoft_app:user', user_id=request.user.id)


@login_required()
def index(request):
    """
    Renders the main page of the site with a list of all registered users.

    :param request: Request object.
    """
    return render(request, 'emphasoft_app/index.html', context={
        'users': User.objects.all().order_by('-last_login'),
    })


@login_required()
def user_page(request, user_id: int):
    """
    Renders a user page.

    :param request: Request object.
    :param user_id: int: The ID of the user whose page you want to display.
    """
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
    """
    Modifies the authenticated user data if the request method is POST,
    or renders the authenticated user data change form otherwise.

    :param request:
    """
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
