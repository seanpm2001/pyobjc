from PyObjCTools.TestSupport import *

import CoreServices


class TestFixMath(TestCase):
    def assert_not_wrapped(self, name):
        self.assertTrue(
            not hasattr(CoreServices, name), "%r exposed in bindings" % (name,)
        )

    def test_not_wrapped(self):
        self.assert_not_wrapped("fixed1")
        self.assert_not_wrapped("fract1")
        self.assert_not_wrapped("positiveInfinity")
        self.assert_not_wrapped("negativeInfinity")
        self.assert_not_wrapped("_IntSaturate")
        self.assert_not_wrapped("FloatToFixed")
        self.assert_not_wrapped("FloatToFract")
        self.assert_not_wrapped("FixedRound")
        self.assert_not_wrapped("FixedSquareRoot")
        self.assert_not_wrapped("FixedTruncate")
        self.assert_not_wrapped("FixedToFract")
        self.assert_not_wrapped("FractToFixed")
        self.assert_not_wrapped("FixedToInt")
        self.assert_not_wrapped("IntToFixed")
        self.assert_not_wrapped("FixedToFloat")
        self.assert_not_wrapped("FractToFloat")
        self.assert_not_wrapped("ColorToFract")
        self.assert_not_wrapped("FractToColor")
        self.assert_not_wrapped("FixRatio")
        self.assert_not_wrapped("FixMul")
        self.assert_not_wrapped("FixRound")
        self.assert_not_wrapped("Fix2Frac")
        self.assert_not_wrapped("Fix2Long")
        self.assert_not_wrapped("Long2Fix")
        self.assert_not_wrapped("Frac2Fix")
        self.assert_not_wrapped("FracMul")
        self.assert_not_wrapped("FixDiv")
        self.assert_not_wrapped("FracDiv")
        self.assert_not_wrapped("FracSqrt")
        self.assert_not_wrapped("FracSin")
        self.assert_not_wrapped("FracCos")
        self.assert_not_wrapped("FixATan2")
        self.assert_not_wrapped("Frac2X")
        self.assert_not_wrapped("Fix2X")
        self.assert_not_wrapped("X2Fix")
        self.assert_not_wrapped("X2Frac")
        self.assert_not_wrapped("WideCompare")
        self.assert_not_wrapped("WideAdd")
        self.assert_not_wrapped("WideSubtract")
        self.assert_not_wrapped("WideNegate")
        self.assert_not_wrapped("WideShift")
        self.assert_not_wrapped("WideSquareRoot")
        self.assert_not_wrapped("WideMultiply")
        self.assert_not_wrapped("WideDivide")
        self.assert_not_wrapped("WideWideDivide")
        self.assert_not_wrapped("WideBitShift")
        self.assert_not_wrapped("UnsignedFixedMulDiv")


if __name__ == "__main__":
    main()
