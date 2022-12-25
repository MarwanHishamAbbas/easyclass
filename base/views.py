from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .forms import MyUserCreationForm
from .models import User

def homePage(request):
    context = {}
    return render(request, 'base/home.html', context)

    
def loginRegisterPage(request):
    form = MyUserCreationForm()
    if request.method == 'POST':
        if 'login' in request.POST:
            email = request.POST.get('email')
            password = request.POST.get('password')
            try:
                user = User.objects.all()
            except:
                print("Can't find the user in the database")
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')

        if 'register' in request.POST:
            form = MyUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.save()
                login(request, user)
                return redirect('home')
    context = {'form': form}

    return render(request, 'base/login_register.html', context)
