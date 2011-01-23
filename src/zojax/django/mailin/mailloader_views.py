import sys, urllib, traceback, os.path

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse

mailloaderFile = os.path.join(os.path.dirname(__file__), 'mailloader.py')


def loader(request):

    return render_to_response("mailin/mailloader.html",
                              context_instance=RequestContext(request))


def loader_py(request):
    data = open(mailloaderFile, 'rb').read()
    response = HttpResponse(data%{'HOSTNAME': request.build_absolute_uri('/')})
    response['Content-Disposition'] = 'attachment; filename="mailloader.py"'
    return response
