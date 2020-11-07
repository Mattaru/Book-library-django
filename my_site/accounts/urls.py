from django.urls import path, reverse_lazy

from allauth.account.views import login, logout

from accounts.views import (
    UserDetail,
    UserProfileUpdate,
    RegisterView,
    # CreateUserProfile,
)


app_name = 'accounts'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('registration/', RegisterView.as_view(
        template_name='pages/user-profile/registration.html',
        success_url=reverse_lazy('p_library:home'),
    ), name='registration'),
    # path('profile-create/', CreateUserProfile.as_view(), name='profile-create'),

    path('user/<int:pk>/', UserDetail.as_view(), name='user_profile'),
    path('user/update/', UserProfileUpdate.as_view(), name='user_update'),
]

