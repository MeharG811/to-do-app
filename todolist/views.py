from django.shortcuts import render,redirect,get_object_or_404
from todolist.models import status_Return

from .models import Tasks
from .forms import TaskForm
from django.db.models import Q,Count
# Create your views here.

def home(request):
    
    status_=status_Return()
    task=Tasks.objects.all()
    task_counts = Tasks.objects.values('status').annotate(count=Count('status')).order_by('status')
    forms={
        "key":1,
        "status_":status_,
        "tasks":task,
        "task_counts":task_counts
    }


    if request.method=="POST":
        print("hello")
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')

    if request.method=="GET":
            query = request.GET.get('query')
            tasks = Tasks.objects.all()
            if query:
                tasks = tasks.filter(
                    Q(title__icontains=query) | Q(description__icontains=query)
                )
                # Initialize counts with zero for each status
                initial_counts = {status: 0 for status in status_.keys()}
                
                # Get the counts from the filtered query
                task_counts_query = tasks.values('status').annotate(count=Count('status')).order_by('status')
                
                # Update the initial counts with the actual counts
                for entry in task_counts_query:
                    initial_counts[entry['status']] = entry['count']
                
                # Prepare task counts in the format required by the template
                task_counts = [{'status': status_, 'count': count} for status_, count in initial_counts.items()]

                    
                forms={
                    "key":1,
                    "status_":status_,
                    "tasks":tasks,
                    "task_counts":task_counts
                }
                return render(request,"index.html",{'forms': forms})
        
    return render(request,"index.html",{'forms': forms})

def edit_task(request,id):
    task = get_object_or_404(Tasks, id=id)
    forms = {}
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a view displaying tasks
    else:
        form = TaskForm(instance=task)  # Populate form with existing task data
    return render(request, 'index.html', {'form': form})
    
def delete_task(request,id):
    status_=status_Return()
    task=get_object_or_404(Tasks,id=id)
    # if request.method == 'POST':
    task.delete()
    return redirect('home')


