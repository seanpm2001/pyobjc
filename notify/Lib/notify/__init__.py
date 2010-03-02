"""
These routines allow processes to exchange stateless notification events.

Notifications are associated with names in a namespace shared by all
clients of the system.  Clients may post notifications for names, and
may monitor names for posted notifications.  Clients may request
notification delivery by a number of different methods.

Clients desiring to monitor names in the notification system must
register with the system, providing a name and other information
required for the desired notification delivery method.  Clients are
given an integer token representing the registration.

Notification delivery is provided on a best-effort basis, but is not
reliable.  Limitations in the service may cause some notifications to
be dropped, particularly under heavily loaded conditions.

Notifications may be coalesced in some cases.  Multiple events posted
for a name in rapid succession may result in a single notification sent
to clients registered for notification for that name.  Clients checking
for changes using the notify_check() routine cannot determine if
more than one event pas been posted since a previous call to 
notify_check() for that name.

"False positives" may occur in notify_check() when used with a token
generated by notify_register_check() due to implementation constraints.
This behavior may vary in future releases.  
"""
__version__="0.1"

NOTIFY_STATUS_OK=0
NOTIFY_STATUS_INVALID_NAME=1
NOTIFY_STATUS_INVALID_TOKEN=2
NOTIFY_STATUS_INVALID_PORT=3
NOTIFY_STATUS_INVALID_FILE=4
NOTIFY_STATUS_INVALID_SIGNAL=5
NOTIFY_STATUS_INVALID_REQUEST=6
NOTIFY_STATUS_NOT_AUTHORIZED=7
NOTIFY_STATUS_FAILED=1000000
NOTIFY_REUSE=0x00000001

from _notify import *