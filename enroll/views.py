from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import Entries_form
from .models import Entries


def get_data(request):
    if request.method == 'POST':
        form_var = Entries_form(request.POST)

        # method 1 to save entered data into table
        # if form_var.is_valid():
        #     form_var.save()

        # method2
        if form_var.is_valid():
            nm = form_var.cleaned_data['name']
            em = form_var.cleaned_data['email']
            ci = form_var.cleaned_data['city']
            reg = Entries(name=nm, email=em, city=ci)
            reg.save()
        form_var = Entries_form()

    else:
        form_var = Entries_form()
    stu = Entries.objects.all()
    return render(request, 'getting.html', {'form': form_var, 'stud': stu})


def delete_data(request, id):
    if request.method == 'POST':
        to_del = Entries.objects.get(pk=id)
        to_del.delete()
        return HttpResponseRedirect('/')


def update_data(request, id):
    if request.method == 'POST':
        to_update = Entries.objects.get(pk=id)
        updated_data = Entries_form(request.POST, instance=to_update)
        if updated_data.is_valid():
            updated_data.save()
    else:
        to_update = Entries.objects.get(pk=id)
    toupdated_data = Entries_form(instance=to_update)
    return render(request, 'update.html', {'toupdated_data': toupdated_data})
