from django.urls import path, reverse_lazy

from allauth.account.views import login, logout

from accounts.views import (
    UserDetail,
    RegisterView,
    CreateUserProfile,
)


app_name = 'accounts'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('registration/', RegisterView.as_view(
        template_name='pages/user-profile/registration.html',
        success_url=reverse_lazy('accounts:profile-create'),
    ), name='registration'),
    path('profile-create/', CreateUserProfile.as_view(), name='profile-create'),

    path('user/<int:pk>/', UserDetail.as_view(), name='user_profile'),
]

