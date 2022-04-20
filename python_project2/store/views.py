from django.shortcuts import render

# Create your views here.

products = [
    {
        'name': 'jeans',
        'brand': 'valentino',
        'description': 'straight leg blue jeans',
        'size': 'Small'
    },
    {
        'name': 't-shirt',
        'brand': 'comme des garcon',
        'description': 'black oversized t-shirt',
        'size': 'medium'
    }
]


def home(request):
    context = {
        'products': products
    }
    return render(request, 'store/home.html', context)


def about(request):
    return render(request, 'store/about.html', {'title': 'About'})

