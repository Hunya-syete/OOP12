from django.urls import path

from myapp.views import user_login, success

urlpatterns = [
 path('login/', user_login, name='login'),
 path('success/', success, name='success'),
]


