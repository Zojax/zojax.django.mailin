##############################################################################
"""

$Id$
"""

class MailInException(Exception):
    """ base mailin exception """


class CheckMessageException(MailInException):
    """ check mail exception """
