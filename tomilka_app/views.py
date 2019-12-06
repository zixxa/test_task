from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'tomilka_app/index.html', {})

def whysotasty(request):
    return render(request, 'tomilka_app/link-1.html', {})

def health(request):
	return render(request, 'tomilka_app/link-2.html', {})

def types (request):
	return render(request, 'tomilka_app/link-3.html', {})

def qar (request):
	return render(request, 'tomilka_app/link-4.html', {})