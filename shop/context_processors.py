from .models import Categories
from django.conf import settings


def categories(request):
    kwargs = {
        "categories": Categories.objects.all(),
    }
    return kwargs