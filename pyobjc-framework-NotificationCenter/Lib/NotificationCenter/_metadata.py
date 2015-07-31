# This file is generated by objective.metadata
#
# Last update: Fri Jul 31 16:47:52 2015

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
constants = '''$$'''
enums = '''$NCUpdateResultFailed@2$NCUpdateResultNewData@0$NCUpdateResultNoData@1$'''
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'NCWidgetController', b'setHasContent:forWidgetWithBundleIdentifier:', {'arguments': {2: {'type': 'Z'}}})
    r(b'NCWidgetListViewController', b'editing', {'retval': {'type': 'Z'}})
    r(b'NCWidgetListViewController', b'hasDividerLines', {'retval': {'type': 'Z'}})
    r(b'NCWidgetListViewController', b'setEditing:', {'arguments': {2: {'type': 'Z'}}})
    r(b'NCWidgetListViewController', b'setHasDividerLines:', {'arguments': {2: {'type': 'Z'}}})
    r(b'NCWidgetListViewController', b'setShowsAddButtonWhenEditing:', {'arguments': {2: {'type': 'Z'}}})
    r(b'NCWidgetListViewController', b'showsAddButtonWhenEditing', {'retval': {'type': 'Z'}})
    r(b'NCWidgetListViewController', b'viewControllerAtRow:makeIfNecessary:', {'arguments': {3: {'type': 'Z'}}})
    r(b'NSObject', b'widgetAllowsEditing', {'retval': {'type': 'Z'}})
    r(b'NSObject', b'widgetMarginInsetsForProposedMarginInsets:', {'retval': {'type': '{NSEdgeInsets=dddd}'}, 'arguments': {2: {'type': '{NSEdgeInsets=dddd}'}}})
    r(b'NSObject', b'widgetPerformUpdateWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': sel32or64(b'I', b'Q')}}}, 'type': '@?'}}})
    r(b'NSObject', b'widgetSearch:searchForTerm:maxResults:', {'arguments': {4: {'type': sel32or64(b'I', b'Q')}}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
