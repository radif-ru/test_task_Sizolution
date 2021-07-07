from django.http import HttpResponse
# from django.views.decorators.cache import cache_page


# Кэширование в mainapp/urls, можно было и здесь оставить,
# но это менее функционально
# @cache_page(60 * 60 * 60, cache="mainapp_cache")
def index(request):
    return HttpResponse("mainapp index")

