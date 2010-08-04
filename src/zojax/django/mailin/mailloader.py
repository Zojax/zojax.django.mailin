#!/usr/bin/env python2.5
"""
Aliases:

(address): |"python path-to-script/mailloader.py http://host-name"


$Id$
"""
import sys, urllib, traceback, os.path, urlparse

MAXSIZE = 0
HOSTNAME = u'%(HOSTNAME)s'


def main(argv):
    file = open('/tmp/mailtransport.log', 'ab')
    try:
        if len(argv) > 1:
            host = argv[1]
        else:
            host = HOSTNAME

        url = urlparse.urljoin(host, 'mailin/mailinTransport')

        print >> file, url

        email = sys.stdin.read()

        print >> file, email

        if (MAXSIZE>0) and (len(email) > MAXSIZE):
            raise Exception('Maximum size exceeded.')

        try:
            t = urllib.urlopen(url, urllib.urlencode({'mail': email}))
            print >> file, t.read()
        except:
            traceback.print_exc(file=file)
            pass

        print >> file, 'done -----------------'
    finally:
        file.close()

if __name__ == '__main__':
    main(sys.argv)

