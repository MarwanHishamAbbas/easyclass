from django.shortcuts import render


def loginPage(request):
    context = {}
    return render(request, 'base/login_register.html', context)
