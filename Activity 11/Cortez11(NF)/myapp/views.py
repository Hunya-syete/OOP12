from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
      form = LoginForm(request.POST)
      if form.is_valid():

         username = form.cleaned_data['username']
         password = form.cleaned_data['password']
         user = authenticate(request, username=username, password=password)
      if user is not None:
         login(request, user)
      return redirect('success')

    else:
      form = LoginForm()
      return render(request, 'login.html', {'form': form})

def success(request):
      return render(request, 'success.html')