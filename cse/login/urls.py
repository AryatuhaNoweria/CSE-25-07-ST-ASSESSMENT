from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),          # Login page
    path('sign-up/', views.sign_up_view, name='sign_up'),  # Sign-up page
]