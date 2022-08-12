from django.shortcuts import render

def hello_world(request):
    return render(request, 'hello_world.html', {})

def home_page(request):
    return render(request, 'home.html', {})