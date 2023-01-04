
from django.shortcuts import render, redirect, get_object_or_404

from .form import PersonCreationForm
from .models import Person, Course


def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_add')
    return render(request, 'form.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'form.html', {'form': form})


# AJAX
def load_course(request):
    department_id = request.GET.get('department_id')
    course = Course.objects.all().filter(department_id=department_id)
    return render(request, 'city_dropdown_list_options.html', {'course': course})