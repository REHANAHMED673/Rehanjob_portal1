from django.urls import path
from . import views

urlpatterns = [

    # Login page
    path("login/", views.login_view, name="login"),

    # Register page
    path("register/", views.register, name="register"),

    # Logout
    path("logout/", views.user_logout, name="logout"),

]