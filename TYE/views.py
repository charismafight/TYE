from django.http import HttpResponse
from django.template import loader
from .models import *


def index(request):
    template = loader.get_template('index.html')
    context = {'archives': Archive.objects.all(), 'videos': Video.objects.all()}

    return HttpResponse(template.render(context, request))
