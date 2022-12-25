from django.shortcuts import render
from .forms import MyUserCreationForm

def homePage(request):
    context = {}
    return render(request, 'base/home.html', context)

    
def loginRegisterPage(request):
    form = MyUserCreationForm()
    context = {'form': form}
    return render(request, 'base/login_register.html', context)
