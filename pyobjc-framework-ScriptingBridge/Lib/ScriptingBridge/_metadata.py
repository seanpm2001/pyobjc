# This file is generated by objective.metadata
#
# Last update: Thu Feb 23 12:19:00 2012

import objc, sys

if sys.maxint > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
constants = '''$$'''
enums = '''$$'''
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r('SBApplication', b'isRunning', {'retval': {'type': 'Z'}})
    r('SBElementArray', b'arrayByApplyingSelector:', {'arguments': {2: {'sel_of_type': b'@@:'}}})
    r('SBElementArray', b'arrayByApplyingSelector:withObject:', {'arguments': {2: {'sel_of_type': b'@@:@'}}})
    r('SBObject', b'sendEvent:id:parameters:', {'variadic': True})
finally:
    objc._updatingMetadata(False)
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r('NSObject', b'eventDidFail:withError:', {'required': True, 'retval': {'type': b'@'}, 'arguments': {2: {'type': 'r^{AEDesc=I^^{OpaqueAEDataStorageType}}'}, 3: {'type': b'@'}}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE