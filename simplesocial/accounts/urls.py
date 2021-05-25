from django.urls import path
from django.contrib.auth import views as auth_views     #we are importing authorization view so we don't mix up with our views
from . import views

app_name ='accounts'

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),     #For logout we don't have template_name bcoz we have default view
    path('signup/', views.SignUp.as_view(), name="signup"),
]
