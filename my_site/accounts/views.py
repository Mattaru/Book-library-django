from django.shortcuts import render
from django.views.generic import (
    FormView,
    ListView,
    DetailView,
    UpdateView,
)
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.http.response import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from allauth.socialaccount.models import SocialAccount

from accounts.forms import UserProfileForm
from accounts.models import UserProfile


class UserDetail(DetailView):
    model = User
    template_name = 'pages/user-profile/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super(UserDetail, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            try:
                context['extra_data'] = SocialAccount.objects.get(
                    provider='github',
                    user=self.request.user
                ).extra_data

            except:
                pass
        return context


class UserProfileUpdate(UpdateView):
    model = UserProfile
    fields = [
        'first_name',
        'last_name',
        'age',
        'avatar',
    ]
    template_name = 'pages/user-profile/user_update.html'
    success_url = reverse_lazy('p_library:home')

    def get_object(self):
        return self.request.user.profile

    def form_valid(self, form):
        super(UserProfileUpdate, self).form_valid(form)
        social = SocialAccount.objects.filter(provider='github', user=self.request.user).first()
        if social:
            social.extra_data['first_name'] = form.instance.first_name
            social.extra_data['last_name'] = form.instance.last_name
            social.extra_data['age'] = form.instance.age
            social.save()
        return HttpResponseRedirect(self.get_success_url())


class RegisterView(FormView):
    form_class = UserCreationForm

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        login(self.request, authenticate(username=username, password=raw_password))
        return super(RegisterView, self).form_valid(form)


# class CreateUserProfile(FormView):
#     form_class = UserProfileForm
#     template_name = 'pages/user-profile/registration.html'
#     success_url = reverse_lazy('p_library:home')
#
#     def dispatch(self, request, *args, **kwargs):
#         if self.request.user.is_anonymous:
#             return HttpResponseRedirect(reverse_lazy('accounts:login'))
#         return super(CreateUserProfile, self).dispatch(request, *args, **kwargs)
#
#     def form_valid(self, form):
#         instance = form.save(commit=False)
#         instance.user = self.request.user
#         instance.save()
#         return super(CreateUserProfile, self).form_valid(form)

