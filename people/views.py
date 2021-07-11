from django.shortcuts import get_object_or_404, render, redirect
from django.conf import settings

from .models import Person
from .forms import PersonForm
from django.contrib import messages


def people_list(request):
  if request.user.is_authenticated:
    people = Person.objects.all().values('id', 'name', 'born_date',
                                         'ddd_private_phone', 'private_phone')
    context = {'people': people}
    return render(request, 'index.html', context)
  else:
    return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))


def person_create(request):
  if request.user.is_authenticated:

    if request.method == "GET":
      form = PersonForm()
      context = {'form': form}
      return render(request, 'person_create.html', context)

    if request.method == "POST":

      data_person = PersonForm(request.POST)

      if data_person.is_valid():

        person = data_person.save(commit=False)

        # make some logic

        person.save()

        messages.success(request, 'Cadastro realizado com sucesso!')

        return redirect('/pessoas/')

      else:

        messages.error(request, 'Por favor, corrigir os erros abaixo.')

        context = {'form': data_person}

        return render(request, 'person_create.html', context)

  else:
    return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))


def person_edit(request, pk):
  if request.user.is_authenticated:
    person = get_object_or_404(Person, id=pk)
    form = PersonForm(instance=person)
    if request.method == "GET":
      context = {'form': form}
      return render(request, 'person_create.html', context)
    if request.method == "POST":
      form = PersonForm(request.POST, instance=person)
      if form.is_valid():
        person = form.save(commit=False)
        person.save()
        messages.success(request, 'Cadastro atualizado com sucesso!')
        return redirect('/pessoas/')
      else:
        messages.error(request, 'Por favor, corrigir os erros abaixo.')
        context = {'form': form}
        return render(request, 'person_create.html', context)

  else:
    return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))


def home(request):
  if request.user.is_authenticated:
    return redirect('/pessoas/')
  else:
    return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
