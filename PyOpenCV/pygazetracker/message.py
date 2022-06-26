# # # # #
# INTERNAL FUNCTIONS
from __init__ import _VERBOSITY
def _message(msgtype, sender, msg):
    if msgtype == u'error':
        raise Exception(u"ERROR in pygazetracker.%s: %s" \
                        % (sender, msg))

    elif msgtype == u'warning' and _VERBOSITY >= 1:
        print(u"WARNING in pygazetracker.%s: %s" % (sender, msg))

    elif msgtype == u'message' and _VERBOSITY >= 2:
        print(u"MSG from pygazetracker.%s: %s" % (sender, msg))

    elif msgtype == u'debug' and _VERBOSITY >= 3:
        print(u"DEBUG pygazetracker.%s: %s" % (sender, msg))