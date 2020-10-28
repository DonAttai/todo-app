from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages


from .models import *
from .forms import TodoForm

# Create your views here.

@login_required(login_url='login')
def index(request):
    todos = Todo.objects.filter(user=request.user)
    form = TodoForm()

    try:
        if request.method == 'POST':
            form = TodoForm(request.POST)
            if form.is_valid():
                instance = form.save()
                instance.user = request.user
                instance.save()
            return redirect('/')

        
    except IntegrityError as e:
        if 'UNIQUE constraint' in str(e.args):
            messages.info(request, 'Todo item already exits in the todo list')
            return redirect('/')
    

    context = {'todos': todos, 'form': form}
    return render(request, 'tasks/index.html', context)


@login_required(login_url='login')
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


@login_required(login_url='login')
def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    
    if request.method == 'POST':
        todo.delete()
        return redirect('/')
    
    context = {'todo': todo, 'title': 'Delete Todo'}
    return render(request, 'tasks/delete.html', context)
    
