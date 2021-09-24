from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        #Note.objects.create(title = title, content= content)(Outro método para salvar os dados)
        note = Note()
        note.title = title
        note.content = content
        note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def update(request, id):
    id = int(id)
    if id != '':
        note = Note.objects.get(id = id)
    return render(request, 'notes/atualiza.html', {"note":note})    

     


def apaga(request, id):
    notedelete = Note.objects.get(id = id)
    return render(request, 'notes/index.html')


