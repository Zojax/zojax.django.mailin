"""

$Id: transport.py 21068 2010-07-27 22:40:31Z bubenkoff $
"""
from email import message_from_string

from utils import log, log_exc
from interfaces import MailInException
from configlet import configlet
from django.shortcuts import render_to_response
from django.http import HttpResponse


class MailInTransport(object):

    def __call__(self, request, *args, **kw):
        mail = request.POST.get('mail') or request.GET.get('mail')
        if not mail:
            return HttpResponse('failed', status=500)

        # convert mail
        try:
            msg = message_from_string(mail.encode('utf-8'))
        except:
            log_exc('Error parsing email')
            return HttpResponse('failed on parsing', status=500)

        # check message for loops, wrong mta hosts, etc
        try:
            configlet.checkMessage(msg, mail, request)
        except MailInException, msg:
            log(str(msg))
            return HttpResponse('failed on checking', status=500)

        # process message
        try:
            configlet.process(msg)
        except MailInException, msg:
            log(str(msg))
            return HttpResponse('failed on processing', status=500)

        return HttpResponse('success')


transport = MailInTransport()
