from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.hashers import make_password, check_password
from .forms import LoginForm, RegisterForm
from .models import User, Gadget, Category, GadgetImage
from django import template


def error_page(request):
    return render(request, 'error_page/error_page.html')


def index(request):
    return render(request, 'home-page/index.html')


def logout(request):
    request.session.flush()
    return redirect(reverse(index))


def catalog(request):
    categories = Category.objects.all()
    return render(request, 'catalog/catalog.html', {'categories': categories})


def login(request):
    # Если метод не POST то возвращаем пустую форму
    if not request.method == 'POST':
        form = LoginForm()
        return render(request, 'auth/login.html', {'form': form})

    # Получаем форму
    form = LoginForm(request.POST)
    # Если форма не валидна то возвращаем пустую форму
    if not form.is_valid():
        form = LoginForm()
        return render(request, 'auth/login.html', {'form': form})

    # Получаем данные из формы
    email = form.cleaned_data["email"]
    password = form.cleaned_data["password"]
    current_user = User.objects.filter(email=email).exists()
    current_user_obj = User.objects.get(email=email)

    # Если пользователь не найден то возвращаем пустую форму с ошибкой
    if not current_user:
        form = LoginForm()
        return render(request, 'auth/login.html', {'form': form, 'error': 'Такого email не существует'})

    # Если пароли не совпали то возвращаем пустую форму с ошибкой
    if not check_password(password, current_user_obj.password):
        form = LoginForm()
        return render(request, 'auth/login.html', {'form': form, 'error': 'Неверный пароль'})

    # Если пользователь найден и пароли совпали - логинемся
    request.session['isLoggedIn'] = 'true'
    # время сессии
    request.session.set_expiry(1200)

    # Редирект на главную
    return redirect(reverse(index))


def register(request):
    if request.method != 'POST':
        form = RegisterForm()
        return render(request, 'auth/register.html', {'form': form})

    form = RegisterForm(request.POST)
    if not form.is_valid():
        form = RegisterForm()
        return render(request, 'auth/register.html', {'form': form})

    try:
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        phone = form.cleaned_data["phone"]
        password = make_password(form.cleaned_data['password'])

        user_email = User.objects.filter(email=email).exists()
        user_phone = User.objects.filter(phone=phone).exists()
        if user_email or user_phone:
            form = RegisterForm()
            return render(request, 'auth/register.html', {'form': form, 'error': 'Этот Email или телефон уже заняты'})
        else:
            User.objects.create(name=name, email=email, phone=phone, password=password)
            request.session['isLoggedIn'] = 'true'
            # время сессии
            request.session.set_expiry(1200)
            return redirect(reverse(index))
    except Exception as error:
        return redirect(reverse(error_page))


def phones(request):
    phones = Gadget.objects.all()
    return render(request, 'catalog/phones/phones.html', {'phones': phones})


def phone_id(request, name):
    current_phone = Gadget.objects.get(name=name)
    images = GadgetImage.objects.filter(gadget_id=current_phone.id)
    return render(request, 'catalog/phones/phone_id.html', {'phone': current_phone, 'images': images})
