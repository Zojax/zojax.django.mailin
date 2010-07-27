# -*- coding: utf-8 -*-

import Bouncers


class ErroMailInDestination(object):

    def process(self, from_hdr, to_hdr, message):
        log('------------- error handler: %s ----------------'%message.get('from',''))

        # find recipient
        recipient = IMailInRecipient(self)
        if recipient is None:
            self.replyError(message)
                #PROJECTNAME, error_templates[2],
                #                    {'portal_email': portal.email_from_address,
                #                     'portal_email_from': portal.email_from_name
                #                     }, message)
            log("Can't find destination location.")
            return

        # check bounce
        bouncedAddresses = Bouncers.ScanMessage(message)

        if bouncedAddresses:
            log('bounced: %s'%bouncedAddresses)
            recipient.bounced(bouncedAddresses, message)
            return
