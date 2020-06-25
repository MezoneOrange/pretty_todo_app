import datetime

from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.http import require_POST

from .models import Todo
from .forms import TodoForm
from .forms import NewTodoForm


def index(request):
    todo_list = Todo.objects.order_by('id')
    #form = TodoForm()
    newtodoform = NewTodoForm()

    mydate = datetime.datetime.now()

    context = {'todo_list': todo_list, 'form': newtodoform, 'mydate': mydate}

    return render(request, 'todo/index.html', context)


@require_POST
def add_todo(request):
    #form = TodoForm(request.POST)
    # todo_9 = Todo.objects.get(pk=9)
    # newtodoform = NewTodoForm(request.POST, instance=todo_9)  # instance is concrete object from db. For updating this object
    newtodoform = NewTodoForm(request.POST)
    if newtodoform.is_valid():
        newtodoform.save()
        # new_todo = Todo(text=form.cleaned_data['text'])
        # new_todo.save()

    return redirect('index')


def complete_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')


def delete_completed(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('index')


def delete_all(request):
    Todo.objects.all().delete()

    return redirect('index')