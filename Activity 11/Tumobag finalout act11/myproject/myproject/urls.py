from django.contrib import admin
from django.urls import path, include
from myapp.views import user_login, success

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("login/", include("django.contrib.auth.urls")),
    path('login/', user_login, name='login'),
    path('success/', success, name='success'),
]