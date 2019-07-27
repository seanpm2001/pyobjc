# This file is generated by objective.metadata
#
# Last update: Sat Jul 27 13:22:26 2019

import objc, sys

if sys.maxsize > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
constants = '''$SNErrorDomain$'''
enums = '''$SNErrorCodeInvalidFormat@3$SNErrorCodeInvalidModel@4$SNErrorCodeOperationFailed@2$SNErrorCodeUnknownError@1$'''
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'NSObject', b'request:didFailWithError:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'request:didProduceResult:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'requestDidComplete:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'SNAudioFileAnalyzer', b'addRequest:withObserver:error:', {'retval': {'type': b'Z'}})
    r(b'SNAudioStreamAnalyzer', b'addRequest:withObserver:error:', {'retval': {'type': b'Z'}})
    r(b'SNClassificationResult', b'timeRange', {'retval': {'type': b'{_CMTimeRange={_CMTime=qiIq}{_CMTime=qiIq}}'}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
