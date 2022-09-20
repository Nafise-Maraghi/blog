from django.urls import path

from .views import SignUpView, login, AllUsers, LogOut


urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('login/', login),
    path('logout/', LogOut.as_view()),
    path('users/', AllUsers.as_view()),
]
