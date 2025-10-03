from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    platillos = [
        {'nombre': 'Pizza Margherita', 'precio': 12.50, 'descripcion': 'La clásica pizza italiana con tomate, mozzarella y albahaca.'},
        {'nombre': 'Hamburguesa Clásica', 'precio': 9.75, 'descripcion': 'Carne de res, lechuga, tomate, cebolla y queso en pan brioche.'},
        {'nombre': 'Ensalada César', 'precio': 8.00, 'descripcion': 'Lechuga romana, crutones, queso parmesano y aderezo César.'}
    ]
    contexto = {'platillos': platillos}
    return render(request, 'index.html', contexto)