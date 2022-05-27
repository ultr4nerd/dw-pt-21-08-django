from django.shortcuts import render, redirect

listas_compras = {}


def mostrar_listas(request):
    """Muestra las listas disponibles"""
    context = {"listas": listas_compras.keys()}
    return render(request, "mostrar_listas.html", context)


def crear_lista(request):
    """Crea una nueva lista vacía"""
    context = {}
    if request.method == 'POST':
        nombre = request.POST['nombre']
        if nombre in listas_compras:
            context["error"] = "Ya existe esta lista"
        else:
            listas_compras[nombre] = []
            return redirect("lista:mostrar_listas")
    return render(request, "crear_lista.html", context)


def mostrar_lista(request, nombre):
    """Muestra el contenido de la lista"""
    lista = listas_compras[nombre]

    if request.method == 'POST':
        producto = request.POST['producto']
        lista.append(producto)

    context = {"lista": lista, "nombre": nombre}
    return render(request, "mostrar_lista.html", context)
