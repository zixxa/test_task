from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'tomilka_app/index.html', {})

def whysotasty(request):
    return render(request, 'tomilka_app/link-1.html', {})

def health(request):
    return render(request, 'tomilka_app/link-2.html', {})

def types (request):
    form={}
    if request.POST:
        print (request.POST.get('name'), request.POST.get('phone'))

    models = {"new_price_camping":"1999 руб.", "old_price_camping":"2500 руб.",
			  "new_price_group": "2499 руб.", "old_price_group":"2499 руб.",
			  "new_price_stock": "2999 руб.", "old_price_stock":"5000 руб."}
    return render(request, 'tomilka_app/link-3.html', context=models)

def qar (request):
	return render(request, 'tomilka_app/link-4.html', {})
