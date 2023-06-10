from django.shortcuts import render, get_object_or_404, redirect
from .models import myModel
from .forms import myModelForm

def index(request):
    my_objects = myModel.objects.all()
    return render(request, 'index.html', {'my_objects': my_objects})

def create(request):
    if request.method == 'POST':
        form = myModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = myModelForm()
    return render(request, 'create.html', {'form': form})

def update(request, pk):
    my_object = get_object_or_404(myModel, pk=pk)
    if request.method == 'POST':
        form = myModelForm(request.POST, instance=my_object)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = myModelForm(instance=my_object)
    return render(request, 'update.html', {'form': form})

def delete(request, pk):
    my_object = get_object_or_404(myModel, pk=pk)
    if request.method == 'POST':
        my_object.delete()
        return redirect('index')
    return render(request, 'delete.html', {'my_object': my_object})
