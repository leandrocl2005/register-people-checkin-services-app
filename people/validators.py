from django.core.exceptions import ValidationError
from .brasilian_cities_list import cities
from .formatters import format_text
import re


def check_city(city):
  formatted_cities = [format_text(c) for c in cities]
  if city not in formatted_cities:
    raise ValidationError("Cidade não encontrada.")


def check_cep(cep: str) -> None:
  if re.sub(r'[\d]+', "", cep):
    raise ValidationError("CEP deve conter apenas dígitos.")
  if len(cep) != 8:
    raise ValidationError("CEP deve conter exatamente 8 dígitos.")


def check_phone(phone: str) -> None:
  if re.sub(r'[\d]+', "", phone):
    raise ValidationError("Telefone deve conter apenas dígitos.")
  if len(phone) < 8 or len(phone) > 9:
    raise ValidationError("Telefone deve conter 8 ou 9 dígitos.")


def check_cpf(cpf: str) -> None:
  if re.sub(r'[\d]+', "", cpf):
    raise ValidationError("CPF deve conter apenas dígitos de 0 a 9.")
  if len(cpf) != 11:
    raise ValidationError("CPF deve ter 11 dígitos.")

  d1 = ((sum([int(a) * b
              for a, b in zip(cpf[:-2], list(range(10, 1, -1)))]) * 10) %
        11) % 10
  d2 = ((sum([int(a) * b
              for a, b in zip(cpf[:-2], list(range(11, 2, -1)))] + [d1 * 2]) *
         10) % 11) % 10
  if not (str(d1) == cpf[-2] and str(d2) == cpf[-1]):
    raise ValidationError("CPF inválido.")
