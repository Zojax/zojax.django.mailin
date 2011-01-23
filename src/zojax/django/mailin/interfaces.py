##############################################################################
"""

$Id: interfaces.py 21068 2010-07-27 22:40:31Z bubenkoff $
"""

class MailInException(Exception):
    """ base mailin exception """


class CheckMessageException(MailInException):
    """ check mail exception """
