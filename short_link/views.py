from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.views import LoginView, LogoutView

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ShortForm
from .models import Urls


def show_hello(request):
    url = Urls.objects.filter(user_id=request.user.id)
    context = {'url': url}
    return render(request, 'basic.html', context)


def profile(request):
    url = Urls.objects.filter(user_id=request.user.id)
    context = {'url': url}
    return render(request, 'profile.html', context)


def redirect_to_orig(request, short_id):
    url = Urls.objects.get(short_id=short_id)
    return redirect(url.httpurl)


@login_required(login_url='main')
def short_link(request):
    if request.method == 'POST':
        form = ShortForm(request.POST)
        if form.is_valid():
            forms = form.save(commit=False)
            forms.user = request.user
            form.save()
            url = Urls.objects.last()
            context = {'form': form, 'url': url}
            return render(request, 'short_succes.html', context)
    else:
        form = ShortForm()
        context = {'form': form}
        return render(request, 'short.html', context)


class Log(LoginView):
    template_name = 'login.html'
    next_page = '/'


class Out(LogoutView):
    template_name = 'logout.html'
    next_page = '/'



class Registr(CreateView):
    form_class = UserCreationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('main')
