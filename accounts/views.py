from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from .forms import UserCarForm
import logging

logger = logging.getLogger(__name__)

def start_page(request):
    return render(request, 'start.html')

def user_login(request):
    if request.method == "POST":
        form = UserCarForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Автомобиль успешно добавлен.')
            return redirect('dashboard')
        else:
            # Для каждой ошибки в форме добавляем отдельное сообщение
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{form.fields[field].label}: {error}")
    else:
        form = UserCarForm()
    return render(request, 'user_login.html', {'form': form})

def dashboard(request):
    return render(request, 'dashboard.html')

def add_car(request):
    return render(request, 'add_car.html')