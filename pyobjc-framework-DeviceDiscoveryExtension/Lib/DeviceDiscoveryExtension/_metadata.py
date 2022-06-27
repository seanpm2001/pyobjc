# This file is generated by objective.metadata
#
# Last update: Sun Jun 26 23:35:04 2022
#
# flake8: noqa

import objc, sys
from typing import NewType

if sys.maxsize > 2**32:

    def sel32or64(a, b):
        return b

else:

    def sel32or64(a, b):
        return a


if objc.arch == "arm64":

    def selAorI(a, b):
        return a

else:

    def selAorI(a, b):
        return b


misc = {}
constants = (
    """$DDDeviceProtocolStringDIAL$DDDeviceProtocolStringInvalid$DDErrorDomain$"""
)
enums = """$DDDeviceCategoryHiFiSpeaker@0$DDDeviceCategoryHiFiSpeakerMultiple@1$DDDeviceCategoryTV@3$DDDeviceCategoryTVWithMediaBox@2$DDDeviceFlagsNone@0$DDDeviceFlagsSupportsAudio@2$DDDeviceFlagsSupportsVideo@4$DDDeviceProtocolDIAL@1$DDDeviceProtocolInvalid@0$DDDeviceStateActivated@20$DDDeviceStateActivating@10$DDDeviceStateAuthorized@25$DDDeviceStateInvalid@0$DDDeviceStateInvalidating@30$DDErrorCodeBadParameter@350001$DDErrorCodeInternal@350004$DDErrorCodeMissingEntitlement@350005$DDErrorCodePermission@350006$DDErrorCodeSuccess@0$DDErrorCodeTimeout@350003$DDErrorCodeUnknown@350000$DDErrorCodeUnsupported@350002$DDEventTypeDeviceChanged@42$DDEventTypeDeviceFound@40$DDEventTypeDeviceLost@41$DDEventTypeDevicesPresentChanged@50$DDEventTypeUnknown@0$"""
misc.update(
    {
        "DDDeviceCategory": NewType("DDDeviceCategory", int),
        "DDDeviceState": NewType("DDDeviceState", int),
        "DDDeviceFlags": NewType("DDDeviceFlags", int),
        "DDEventType": NewType("DDEventType", int),
        "DDDeviceProtocol": NewType("DDDeviceProtocol", int),
        "DDErrorCode": NewType("DDErrorCode", int),
    }
)
misc.update({})
misc.update({})
functions = {
    "DDDeviceFlagsToString": (b"@Q",),
    "DDDeviceStateToString": (b"@q",),
    "DDDeviceProtocolToString": (b"@q",),
    "DDDeviceCategoryToString": (b"@q",),
    "DDEventTypeToString": (b"@q",),
}
aliases = {"dd_os_ownership": "strong"}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b"DDEventDevicesPresent", b"devicesPresent", {"retval": {"type": b"Z"}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
