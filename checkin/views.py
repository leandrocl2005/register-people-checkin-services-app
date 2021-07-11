from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ChangeCompanionForm, OtherPeopleCheckinForm, PatientCheckinForm

from .models import CompanionCheckin, OtherPeopleCheckin, PatientCheckin


def checkin_exists(person):

  # check if companion have a active checkin
  person_already_in_checkin = CompanionCheckin.objects.filter(
      person=person, active=True).first()
  if person_already_in_checkin:
    return False

  # check if patient have a active checkin
  person_already_in_checkin = PatientCheckin.objects.filter(
      person=person, active=True).first()
  if person_already_in_checkin:
    return False

  # check if patient have a active checkin
  person_already_in_checkin = OtherPeopleCheckin.objects.filter(
      person=person, active=True).first()
  if person_already_in_checkin:
    return False

  return True


# Create your views here.
@login_required
def checkins_pacients_list(request):
  checkins = PatientCheckin.objects.all().values('id', 'person__name',
                                                 'companion__name', 'active',
                                                 'created_at')
  context = {"checkins": checkins}
  return render(request, 'checkins_patient_list.html', context)


@login_required
def checkins_pacients_create(request):

  form = PatientCheckinForm()

  if request.method == "GET":
    return render(request, 'checkins_patient_create.html', {'form': form})

  if request.method == "POST":
    form = PatientCheckinForm(request.POST)
    if form.is_valid():

      checkin = form.save(commit=False)

      if not checkin_exists(checkin.person):
        messages.error(
            request,
            'Existem um checkin em aberto para esse paciente! Favor fechar.')
        return render(request, 'checkins_patient_create.html', {'form': form})

      if not checkin_exists(checkin.companion):
        messages.error(
            request,
            'Existem um checkin em aberto para esse acompanhante! Favor fechar.'
        )
        return render(request, 'checkins_patient_create.html', {'form': form})

      checkin.save()

      # make automatica companion checkin
      checkin_companion = CompanionCheckin(person=checkin.companion,
                                           patient=checkin.person)
      checkin_companion.save()

      messages.success(request, 'Checkin realizado com sucesso!')
      return redirect('/checkins/pacientes/')
    else:
      messages.error(request, "Checkin não realizado.")
      return render(request, 'checkins_patient_create.html', {'form': form})

  messages.error("Algo deu errado")
  return redirect('/checkins/pacientes/')


@login_required
def checkins_pacients_edit(request, pk):

  checkin = get_object_or_404(PatientCheckin, id=pk)

  if not checkin.active:
    messages.error(request,
                   "O checkin já está fechado e não pode ser editado.")
    return redirect("/checkins/pacientes/")

  form = PatientCheckinForm(instance=checkin)
  if request.method == "GET":
    context = {'form': form}
    return render(request, 'checkins_patient_create.html', context)
  if request.method == "POST":
    print(request.POST)
    form = PatientCheckinForm(request.POST, instance=checkin)
    if form.is_valid():
      checkin = form.save(commit=False)
      checkin.save()
      messages.success(request, 'Checkin atualizado com sucesso!')
      return redirect("/checkins/pacientes/")
    else:
      messages.error(request, 'Falha ao atualizar o checkin.')
      context = {'form': form}
      return render(request, 'checkins_patient_create.html', context)
  messages.error(request, 'Algo deu errado.')
  return redirect('/checkins/pacientes/')


@login_required
def checkins_pacients_close(request, pk):

  if request.method == "GET":
    messages.error(request, "Método não é permitido")
    return redirect('/checkins/pacientes/')

  if request.method == "POST":
    try:
      checkin = PatientCheckin.objects.get(id=pk)
    except PatientCheckin.DoesNotExist:
      checkin = None
    if checkin:
      checkin.active = False
      checkin.save()
      print(checkin.companion)
      # ao fechar o do paciente, fechar automaticamente o do acompanhante
      checkin_companion = CompanionCheckin.objects.filter(
          person=checkin.companion, active=True).first()
      checkin_companion.active = False
      checkin_companion.save()

      messages.success(request, "Checkin fechado com sucesso!")

      return redirect('/checkins/pacientes/')
    else:
      messages.error(request, "Checkin não encontrado para fechamento")
      return redirect('/checkins/pacientes/')
  messages.error(request, "Algo deu errado.")
  return redirect('/checkins/pacientes/')


@login_required
def checkins_companions_list(request):
  checkins = CompanionCheckin.objects.all().values('id', 'person__name',
                                                   'patient__name', 'active',
                                                   'created_at')
  context = {"checkins": checkins}
  return render(request, 'checkins_companion_list.html', context)


@login_required
def checkins_others_list(request):
  checkins = OtherPeopleCheckin.objects.all().values('id', 'person__name',
                                                     'active', 'created_at')
  context = {"checkins": checkins}
  return render(request, 'checkins_other_list.html', context)


@login_required
def checkins_others_edit(request, pk):
  checkin = get_object_or_404(OtherPeopleCheckin, id=pk)
  if not checkin.active:
    messages.error(request,
                   "O checkin já está fechado e não pode ser editado.")
    return redirect("/checkins/outros/")
  form = OtherPeopleCheckinForm(instance=checkin)

  if request.method == "GET":
    context = {'form': form}
    return render(request, 'checkins_other_create.html', context)

  if request.method == "POST":
    form = OtherPeopleCheckinForm(request.POST, instance=checkin)

    if form.is_valid():
      checkin = form.save(commit=False)
      checkin.save()
      messages.success(request, 'Checkin atualizado com sucesso!')
      return redirect("/checkins/outros/")
    else:
      messages.error(request, 'Falha ao atualizar o checkin.')
      context = {'form': form}
      return render(request, 'checkins_other_create.html', context)
  messages.error(request, 'Algo deu errado.')
  return redirect('/checkins/outros/')


@login_required
def checkins_others_create(request):

  form = OtherPeopleCheckinForm()

  if request.method == "GET":

    return render(request, 'checkins_other_create.html', {'form': form})

  if request.method == "POST":

    form = OtherPeopleCheckinForm(request.POST)

    if form.is_valid():

      checkin = form.save(commit=False)

      if not checkin_exists(checkin.person):
        messages.error(
            request,
            'Existem um checkin em aberto para essa pessoa! Favor fechar.')
        return render(request, 'checkins_other_create.html', {'form': form})

      checkin.save()

      messages.success(request, 'Checkin realizado com sucesso!')

      return redirect('/checkins/outros/')

    else:

      messages.error(request, "Checkin não realizado.")

      return render(request, 'checkins_other_create.html', {'form': form})

  messages.error(request, 'Algo deu errado.')
  return redirect('/checkins/outros/')


@login_required
def checkins_others_close(request, pk):

  if request.method == "GET":
    messages.error(request, "Método não é permitido")
    return redirect('/checkins/pacientes/')

  if request.method == "POST":
    try:
      checkin = OtherPeopleCheckin.objects.get(id=pk)
    except OtherPeopleCheckin.DoesNotExist:
      checkin = None
    if checkin:
      checkin.active = False
      checkin.save()

      messages.success(request, "Checkin fechado com sucesso!")

      return redirect('/checkins/outros/')

    else:
      messages.error(request, "Checkin não encontrado para fechamento")
      return redirect('/checkins/outros/')

  messages.error(request, "Algo deu errado.")
  return redirect('/checkins/outros/')


@login_required
def checkins_change_companion(request):

  form = ChangeCompanionForm()

  if request.method == "GET":
    return render(request, 'checkins_change_companion.html', {'form': form})

  if request.method == "POST":

    form = ChangeCompanionForm(request.POST)

    if form.is_valid():

      change_checkin = form.save(commit=False)

      if not checkin_exists(change_checkin.new_companion):
        messages.error(
            request,
            'Existem um checkin em aberto para esse acompanhante! Favor fechar.'
        )
        return render(request, 'checkins_change_companion.html',
                      {'form': form})

      # update patient checkin
      try:
        patient_checkin = PatientCheckin.objects.get(
            id=change_checkin.checkin.id)
      except Exception:
        messages.error(request, "Checkin de paciente não encontrado!")
        return redirect("/checkins/pacientes/")

      # close companion checkin
      try:
        companion_checkin = CompanionCheckin.objects.filter(
            person=patient_checkin.companion, active=True).first()
      except Exception:
        messages.error(request,
                       "Checkin do acompanhante antigo não encontrado!")
        return redirect("/checkins/pacientes/")

      companion_checkin.active = False
      companion_checkin.save()
      patient_checkin.companion = change_checkin.new_companion
      patient_checkin.save()

      # open new companion checkin
      try:
        new_companion_checkin = CompanionCheckin(
            person=change_checkin.new_companion,
            patient=change_checkin.checkin.person)
        new_companion_checkin.save()
      except Exception:
        messages.error(request,
                       "Falha ao registrar checkin de novo acompanhante.")

      change_checkin.save()
      messages.success(request, 'Checkin alterado com sucesso!')
      return redirect('/checkins/pacientes/')
    else:
      messages.error(
          "Falha ao alterar checkin. Por favor, cheque os campos do formulário"
      )
      return render(request, 'checkins_change_companion.html', {'form': form})
  messages.error(request, 'Algo deu errado.')
  return redirect('/checkins/outros/')
