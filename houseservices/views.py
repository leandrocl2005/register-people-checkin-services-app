from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.http import JsonResponse

from .forms import HouseServicesForm

from .models import HouseServices


# Create your views here.
@login_required
def house_services_list(request):
    house_services = HouseServices.objects.all()
    context = {"house_services": house_services}
    return render(request, 'house_services_list.html', context)


@login_required
def house_services_create(request):
    form = HouseServicesForm()

    if request.method == "GET":
        return render(request, 'house_services_create.html', {'form': form})

    if request.method == "POST":
        form = HouseServicesForm(request.POST)
        if form.is_valid():

            checkin = form.save(commit=False)

            # make some extra validations or other rules

            checkin.save()

            messages.success(request, 'Serviço cadastrado com sucesso!')

            return redirect('/servicos-da-casa/')
        else:
            messages.error(request, "Erro ao cadastrar serviço.")
            return render(request, 'house_services_create.html',
                          {'form': form})

    messages.error("Algo deu errado")
    return redirect('/servicos-da-casa/')


@login_required
def house_services_edit(request, pk):

    service = get_object_or_404(HouseServices, id=pk)

    form = HouseServicesForm(instance=service)

    if request.method == "GET":
        context = {'form': form}
        return render(request, 'house_services_create.html', context)

    if request.method == "POST":

        form = HouseServicesForm(request.POST, instance=service)

        if form.is_valid():

            checkin = form.save(commit=False)

            # make some extra validations or roles

            checkin.save()

            messages.success(request, 'Serviço atualizado com sucesso!')

            return redirect("/servicos-da-casa/")

        else:

            messages.error(request, 'Falha ao atualizar o serviço.')

            context = {'form': form}

            return render(request, 'house_services_create.html', context)

    messages.error(request, 'Algo deu errado.')

    return redirect('/servicos-da-casa/')


@login_required
@require_http_methods(["POST"])
def house_services_delete(request, pk):

    try:
        service = HouseServices.objects.get(id=pk)
        service.delete()
        messages.success(request, "Serviço deletado com sucesso!")
    except Exception:
        messages.error(request, "Erro ao deletar serviço!")
    return redirect('/servicos-da-casa/')
