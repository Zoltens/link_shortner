from django.contrib import messages

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ShortForm, LoginForm, CreateForm
from .models import Urls


def index(request):
    return render(request, 'basic.html')


def profile(request):
    if request.user.is_authenticated:
        url = Urls.objects.filter(user_id=request.user.id)
        context = {'url': url}
        return render(request, 'profile.html', context)
    else:
        messages.add_message(request, messages.INFO, message='Извините, нужно войти, '
                                                             'чтобы просмотреть историю.')
        return render(request, 'basic.html')


def redirect_to_orig(request, short_id):
    url = Urls.objects.get(short_id=short_id)
    return redirect(url.httpurl)


def short_succes(request):
    url = Urls.objects.last()
    context = {'url': url}
    return render(request, 'short_succes.html', context)


# @login_required(login_url='login')
def short_link(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ShortForm(request.POST)
            if form.is_valid():
                forms = form.save(commit=False)
                forms.user = request.user
                form.save()
                return redirect('short_succes')
        else:
            form = ShortForm()
        context = {'form': form}
        return render(request, 'short.html', context)
    else:
        messages.add_message(request, messages.INFO, message='Извините, нужно войти или зарегистрироваться, '
                                                             'чтобы использовать '
                                                             'приложение.')
        return render(request, 'basic.html')


def delete_link(request, pk):
    link = Urls.objects.filter(id=pk)
    link.delete()
    return redirect('profile')


class LoginUser(LoginView):
    authentication_form = LoginForm
    template_name = 'login.html'
    next_page = '/'


class LogoutUser(LogoutView):
    next_page = '/'


class RegistrUser(SuccessMessageMixin, CreateView):
    form_class = CreateForm
    template_name = 'registration.html'
    success_url = reverse_lazy('index')
    success_message = 'Вы зарегистрировались как %(username)s.'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            username=self.object.username,
        )
