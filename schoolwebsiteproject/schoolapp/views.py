from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login as auth_login
# from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.http import HttpResponse


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered")
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.success(request, "Registration successful. You can now log in.")
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('register')

    return render(request, "register.html")

def home(request):
    return render(request, "home.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('form')
        else:
            messages.error(request, 'Invalid login credentials')
            return render(request, 'login.html')

    return render(request, "login.html")



def form(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, 'form.html', {'username': username})
    else:
        return redirect('login')


def formfill(request):
    username = request.user.username  # Assuming the username is associated with the user
    context = {'username': username}

    if request.method == 'POST':
        messages.info(request, "Order Placed")
        return redirect('data')

    return render(request, "formfill.html", context)


def logout(request):
    username = request.user.username  # Assuming the username is associated with the user
    context = {'username': username}
    return render(request, 'logout.html', context)


from django.shortcuts import render

def data(request):
    username = request.user.username  # Assuming the username is associated with the user
    context = {'username': username}

    return render(request, 'data.html', context)

