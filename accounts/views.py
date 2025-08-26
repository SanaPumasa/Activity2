from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .models import User


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    all_users = User.objects.all()

    context = {
        'form': form,
        'all_users': all_users,
    }

    return render(request, "register.html", context)


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, username=email, password=password)

            if user is not None:
                return redirect('list_view')

            else:
                form.add_error(None, "Invalid email or password.")
        else:
            form.add_error(None, "Invalid email or password.")
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)