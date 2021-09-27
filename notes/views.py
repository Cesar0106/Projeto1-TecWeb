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


#Documentação de django de metodos de atualização e apagar. Tópicos utilizados :
#Updating multiple objects at once(https://docs.djangoproject.com/en/3.2/topics/db/queries/#updating-multiple-objects-at-once)
#Deleting objects(https://docs.djangoproject.com/en/3.2/topics/db/queries/#deleting-objects)
def update(request, id):
    if request.method == 'POST':
        inputtitle = request.POST.get('titulo')
        inputcontent = request.POST.get('detalhes')
        Note.objects.filter(id = id).update(title = inputtitle, content = inputcontent)
        return redirect('index')
    else:
        note = Note.objects.get(id = id)
        return render(request, 'notes/index.html', {"note":note})

     


def delete(request, id):
    request.method == 'POST'
    Note.objects.filter(id = id).delete()
    return redirect('index')



