from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import UserProfile

from .forms import UserLoginForm, UserSignUpForm

def login_view(request):
    login_form = UserLoginForm(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('reservas:salones')
        else:
            messages.warning(request, 'Usuario o contraseña incorrectos')
            return render(request, "login.html")
    else:
        messages.error(request, login_form.errors)
        return render(request, "login.html")

def register_view(request):
    return render(request, "registro.html")

def saveregister_view(request):
    signup_form = UserSignUpForm(request.POST, request.FILES or None)
    if signup_form.is_valid():
        username = signup_form.cleaned_data.get('username')
        email = signup_form.cleaned_data.get('email')
        first_name = signup_form.cleaned_data.get('first_name')
        last_name = signup_form.cleaned_data.get('last_name')
        phone = signup_form.cleaned_data.get('phone')
        password = signup_form.cleaned_data.get('password')
        try:
            user = get_user_model().objects.create(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                password=make_password(password),
                is_active=True
            )
            login(request, user)
            return redirect('reservas:salones')

        except Exception as e:
            print(e)
            return JsonResponse({'detail': f'{e}'})
    else:
        messages.error(request, signup_form.errors)
        return redirect('users:register')
    
def logout_view(request):
    logout(request)
    return redirect('/')