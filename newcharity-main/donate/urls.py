from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path ('blog/', views.blog, name = "blog"),
    path ('emailotp/', views.emailotp, name = "emailotp"),
    path ('email/', views.email, name = "email"),
    path ('vote/', views.vote, name = "vote"),
]