from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import *
from myapp.forms import *

def autor_lista(request):
    autores = Autor.objects.all()
    for i in autores:
        print(i)
        return render (request, 'autor/lista_autor.html', {
            'autores': autores
        })
    
def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Lista_Autores')
    else:
        form = AutorForm()
    return render(request, 'autor/crear.html', {'form':form})

def autor_modificar(request, pk):
    try:
        autor = Autor.objects.get(pk=pk)
    except Autor.DoesNotExist:
        return redirect('404')
        
    if request.method == "POST":
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('Lista_Autores')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'autor/modificar.html', {'form': form})

def autor_eliminar(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == "POST":
        autor.delete()
        return redirect('Lista_Autores')
    return render(request, 'autor/eliminar.html', {'autor': autor})

def obra_lista(request):
    obras = Obra.objects.all()
    return render(request, 'obra/lista_obra.html', {'obras': obras})

def crear_obra(request):
    if request.method == 'POST':
        form = ObraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Lista_Obras')
    else:
        form = ObraForm()
    return render(request, 'obra/crear.html', {'form': form})

def obra_modificar(request, pk):
    try:
        obra = Obra.objects.get(pk=pk)
    except Obra.DoesNotExist:
        return redirect('404')
        
    if request.method == "POST":
        form = ObraForm(request.POST, instance=obra)
        if form.is_valid():
            form.save()
            return redirect('Lista_Obras')
    else:
        form = ObraForm(instance=obra)
    return render(request, 'obra/modificar.html', {'form': form})

def obra_eliminar(request, pk):
    obra = get_object_or_404(Obra, pk=pk)
    if request.method == "POST":
        obra.delete()
        return redirect('Lista_Obras')
    return render(request, 'obra/eliminar.html', {'obra': obra})