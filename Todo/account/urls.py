from django.urls import path


from . import views

urlpatterns = [
    path('signup', views.create_user, name='signup'),
    path('login', views.AuthLoginUser.as_view(), name='login')
]
