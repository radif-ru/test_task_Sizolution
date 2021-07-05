import json

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from linksapp.forms import CheckStructureForm
from parsers.structure import parse_site


def index(request: HttpRequest) -> HttpResponse:
    """ Блок работы со ссылками
    1. /structure GET запрос, В ответ должен прийти словарь с количеством
    каждого типа HTML-тэгов (например {"html": 1, "head": 1, "body": 1,
    "p": 10, "img": 2}) для сайта freestylo.ru
    2. /structure?link=<ссылка> То же, что и выше, но теперь сайт задается
    в запросе
    3. /structure?link=<ссылка>&tags=html,img То же что и выше,
    но теперь помимо ссылки задается массив тэгов через запятую,
    которые нужно вернуть в ответе
    4. /check_structure POST запрос вида
    `{"link": "freestylo.ru", "structure": {"html": 1, "head": 1, "body": 1,
    "p": 10, "img": 2}}` Который для данный ссылки проверяет структуру html
    тэгов. В ответ должно приходить `{"is_correct": True}` если все верно и
    `{"is_correct": False, "difference": {"p": 2, "img": 1}}`  если есть
    ошибки, где difference - это разница структур.
    Например, если верная структура - `{"html": 1, "head": 1, "body": 1,
    "p": 4}` а передавалась структура `{"html": 1, "head": 1, "body": 1,
    "p": 2, "img": 1}` то разница будет `{"p": 2, "img": 1}`
    :param request:
    :return:
    """
    if request.GET:
        link = request.GET.get('link', '')
        tags = request.GET.get('tags', '')
        if link and tags:
            data = parse_site(
                url=correct_url(link), tags=tags)
        elif link:
            data = parse_site(correct_url(link))
        else:
            data = parse_site('https://freestylo.ru')
    return HttpResponse(json.dumps(data))


def check_structure(request):
    if request.method == 'POST':
        form = CheckStructureForm(request.POST)
        if form.is_valid():
            raw_structure = json.loads(request.POST.get('check_structure', ''))
            link = correct_url(raw_structure['link'])
            structure = raw_structure['structure']
            data = parse_site(link)

            new_dict = {}
            for tag in data.keys():
                if tag in structure:
                    value = abs(data[tag] - structure[tag])
                    if value:
                        new_dict[tag] = value
                else:
                    new_dict[tag] = data[tag]

            if new_dict:
                result_response = {"is_correct": False, "difference": new_dict}
            else:
                result_response = {"is_correct": True}
            return HttpResponse(json.dumps(result_response))
        return HttpResponse('form is not valid')
    else:
        form = CheckStructureForm

    return render(request, 'index.html', {'form': form})


def correct_url(url: str) -> str:
    """
    Корректировка ссылок
    :param url: ссылка
    :return:
    """
    if url[:3] != 'http' or url[:4] != '':
        return f'http://{url}'
