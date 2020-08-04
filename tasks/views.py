from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from .models import *
from .forms import TodoForm

# Create your views here.

@login_required(login_url='login')
def index(request):
    todos = Todo.objects.all()
    form = TodoForm

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')


    context = {'todos': todos, 'form': form}
    return render(request, 'tasks/index.html', context)



def update(request, pk):
    todo = Todo.objects.get(id=pk)

    form = TodoForm(instance=todo)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form, 'title': 'Update Todo'}


    return render(request, 'tasks/update.html', context)

def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    
    if request.method == 'POST':
        todo.delete()
        return redirect('/')
    
    context = {'todo': todo, 'title': 'Delete Todo'}
    return render(request, 'tasks/delete.html', context)
    
