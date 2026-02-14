from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
# Create your views here.

from .forms import UserRegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def tasklist(request):
    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        if task_name:
            Task.objects.create(user=request.user, title=task_name)
        return redirect('tasklist')

    # Order by creation time, oldest first → নতুন add হলে নিচে show হবে
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'tasks/tasklist.html', {'tasks': tasks})


def register(request):
    if request.method == 'POST':
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            messages.success(request, f'Account created successfully!')
            return redirect('login')
    else:
        form= UserRegisterForm()
    return render(request, 'tasks/register.html', {'form': form})
        

@login_required
def profile_view(request):
    return render(request, 'tasks/profile.html')


@login_required
def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.complete = not task.complete  # toggle
    task.save()
    return redirect("tasklist")

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return redirect("tasklist")