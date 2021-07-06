import json
from random import choice
from string import ascii_uppercase
from hashlib import sha256

from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render

from authapp.models import SizolutionUser


# Блок авторизации
from .forms import SizolutionUserForm


def index(request: HttpRequest) -> HttpResponse:
    """ Блок авторизации
    1. /login?phone=<телефон> GET запрос с номером телефона,
    в ответ должен прийти 6-значный код
    2.  /login POST запрос вида {"phone": "+71111111111", "code": "QWDCR4"} -
    в ответ должен прийти {"status": "OK"} если код верный и
    {"status": "Fail"} если код не верный. Можно хранить коды для авторизации
    в коде, не используя базу данных или кэш хранилища для этого
    :param request: запрос от пользователя
    :return: string 6-значный код или json статус возвращаемый пользователю
    """
    if request.method == 'POST':
        form = SizolutionUserForm(request.POST)
        if form.is_valid():
            phone_number = correct_num(request.POST.get('phone_number', ''))
            phone_code_input = code_encryption(
                request.POST.get('phone_code', ''))
            phone_code = SizolutionUser.objects\
                .filter(phone_number=phone_number).first()
            if phone_code and phone_code_input == phone_code.phone_code:
                return HttpResponse(json.dumps({"status": "OK"}))
        return HttpResponse(json.dumps({"status": "Fail"}))

    elif request.GET and request.GET.get('phone', ''):
        phone_number = correct_num(request.GET.get('phone', ''))
        phone_code = phone_code_generate(6)
        obj, created = SizolutionUser.objects.update_or_create(
            phone_number=phone_number,
            defaults={
                'phone_code': code_encryption(phone_code),
                'status': True,
            }
        )
        return HttpResponse(f'{phone_code}')
    else:
        form = SizolutionUserForm

    return render(request, './index.html', {'form': form})


def correct_num(phone_number: str) -> str:
    """ Функция для корректировки номера
    :param string phone_number: номер, полученный от пользователя
    :return: string исправленный номер
    """
    if phone_number[0] == ' ':
        phone_number = phone_number.replace(' ', '+', 1)
    return phone_number


def phone_code_generate(num=6) -> str:
    """ Генерация кода, по умолчанию из 6 символов
    :param num: int количество символов
    :return: string сгенерированный код
    """
    return ''.join(choice(ascii_uppercase) for i in range(num))


def code_encryption(phone_code: str) -> str:
    """ Генерация хэша с солью
    :param phone_code: string исходная строка
    :return: string зашифрованная строка
    """
    salt = 'example_salt'
    hash_phone_code = sha256(f'{salt}{phone_code}'.encode())
    return hash_phone_code.hexdigest()
