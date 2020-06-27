# This file is generated by objective.metadata
#
# Last update: Sat Jun 27 16:39:46 2020
#
# flake8: noqa

import objc, sys

if sys.maxsize > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a

misc = {
}
constants = '''$$'''
enums = '''$UNNotificationContentExtensionMediaPlayPauseButtonTypeDefault@1$UNNotificationContentExtensionMediaPlayPauseButtonTypeNone@0$UNNotificationContentExtensionMediaPlayPauseButtonTypeOverlay@2$UNNotificationContentExtensionResponseOptionDismiss@1$UNNotificationContentExtensionResponseOptionDismissAndForwardAction@2$UNNotificationContentExtensionResponseOptionDoNotDismiss@0$'''
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'NSObject', b'didReceiveNotification:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'didReceiveNotificationResponse:completionHandler:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'Q'}}}, 'type': '@?'}}})
    r(b'NSObject', b'mediaPause', {'required': False, 'retval': {'type': b'v'}})
    r(b'NSObject', b'mediaPlay', {'required': False, 'retval': {'type': b'v'}})
    r(b'NSObject', b'mediaPlayPauseButtonFrame', {'required': False, 'retval': {'type': b'{CGRect={CGPoint=dd}{CGSize=dd}}'}})
    r(b'NSObject', b'mediaPlayPauseButtonTintColor', {'required': False, 'retval': {'type': b'@'}})
    r(b'NSObject', b'mediaPlayPauseButtonType', {'required': False, 'retval': {'type': b'Q'}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE