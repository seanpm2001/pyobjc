import sys
from PyObjCTools.TestSupport import *


if sys.maxsize > 2 ** 32:
    import MapKit

    class TestMKLocalSearchCompleter(TestCase):
        def testConstants(self):
            self.assertEqual(MapKit.MKSearchCompletionFilterTypeLocationsAndQueries, 0)
            self.assertEqual(MapKit.MKSearchCompletionFilterTypeLocationsOnly, 1)

            self.assertEqual(MapKit.MKLocalSearchCompleterResultTypeAddress, 1 << 0)
            self.assertEqual(
                MapKit.MKLocalSearchCompleterResultTypePointOfInterest, 1 << 1
            )
            self.assertEqual(MapKit.MKLocalSearchCompleterResultTypeQuery, 1 << 2)

        @min_os_level("10.11")
        def testMethods(self):
            self.assertResultIsBOOL(MapKit.MKLocalSearchCompleter.isSearching)

        @min_sdk_level("10.12")
        def testProtocols(self):
            objc.protocolNamed("MKLocalSearchCompleterDelegate")


if __name__ == "__main__":
    main()
