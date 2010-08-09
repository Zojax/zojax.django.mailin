##############################################################################
"""

$Id$
"""
import copy
from rwproperty import getproperty, setproperty
from email.Utils import parseaddr

from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from utils import log_exc
from interfaces import MailInException


registry = {}


class MailInAwareDestination(object):

    def __init__(self, address):
        self.address = address

    def register(self):
        if not self.address:
            return

        if registry.get(self.address) is not None:
            raise MailInException(
                'Mail-in email address already in use: %s'%self.address)
        registry[self.address] = self

    def unregister(self):
        del registry[self.address]

    @getproperty
    def enabled(self):
        return self.__dict__.get('enabled', False)

    @setproperty
    def enabled(self, value):
        if value:
            self.register()
        else:
            self.unregister()

        self.__dict__['enabled'] = value

    @getproperty
    def address(self):
        return self.__dict__.get('address', u'')

    @setproperty
    def address(self, value):
        if self.enabled:
            self.unregister()
            self.__dict__['address'] = value
            self.register()
        else:
            self.__dict__['address'] = value

    def process(self, message):
        # find principal
        from_hdr = parseaddr(message['From'])[1].lower()
        try:
            principal = User.objects.get(email=from_hdr)
        except User.DoesNotExist:
            # member not found
            raise MailInException('Member not found: %s'%from_hdr)

        # deliver message
        try:
            self.processRecipient(principal, message)
        except Exception, e:
            log_exc()
            raise MailInException(e)

    def processRecipient(self, principal, message):
        raise NotImplementedError()
