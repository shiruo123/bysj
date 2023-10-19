"""
URL configuration for bysj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path("admin", views.admin, name="admin"),
    path("admin/delete_data", views.delete_data, name='delete_data'),
    path("admin/update_data", views.update_data, name='update_data'),
    path("admin/create_data", views.create_data, name='create_data'),
    path("", views.main, name="main"),
    path("login", views.login_html, name="login"),
    path("login/login_is", views.login_panduan, name="login_is"),
    path("login/pwd_update_html", views.pwd_update_html, name="pwd_update_html"),
    path("login/pwd_pudate", views.pwd_update, name="pwd_update"),
    path("login/new_account_html", views.new_account_html, name="new_account_html"),
    path("login/new_account", views.new_account, name="new_account"),
    path("login/login_out", views.login_out, name="login_out"),
    path("iframe1", views.iframe1, name="iframe1"),
    path("kaoshi/id=<kaoshi_id>", views.kaoshi, name="kaoshi"),
    path("chengji/id=<kaoshi_id>/daan=<daans>", views.chengji, name="chengji"),
]
