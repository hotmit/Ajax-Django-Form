from django.shortcuts import render
from ajax_django_form.human.models import PunyHuman


def list_human(request):
    context = {
        'data': PunyHuman.objects.all()
    }

    return render(request, 'human/view_human.html', context)


def create_human(request):
    return None


def update_human(request):
    return None