from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = "account"
urlpatterns = [
    path('signup/', views.register, name="signup"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/',LogoutView.as_view(), name="logout"),
    path('',views.index, name='index'),
]