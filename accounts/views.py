from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView
from django.core.paginator import Paginator


class UserProfileView(DetailView):
    model = User
    template_name = 'accounts/user_profile.html'
    context_object_name = 'user'


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('posts:post-list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})