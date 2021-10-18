# This file contains the automated unit testing for both functions

import unittest
from timeCalc import calc_charge
from timeCalc import check_input

class TestTimeCalc(unittest.TestCase):
    def test_calc_charge(self):
        # testing that calculations work as expected
        self.assertAlmostEqual(calc_charge('5pm', '1am', '8pm'), 84)
        self.assertAlmostEqual(calc_charge('7pm', '4am', '10pm'), 116)
        self.assertAlmostEqual(calc_charge('6pm', '11pm', '9pm'), 52)
        self.assertAlmostEqual(calc_charge('6pm', '9pm', '9pm'), 36)

        # testing that the times given make sense
        self.assertRaises(ValueError, calc_charge, '33pm', '2am', '8pm')
        self.assertRaises(ValueError, calc_charge, '6pm', '72am', '9pm')
        self.assertRaises(ValueError, calc_charge, '5pm', '1am', '88pm')


    def test_check_input(self):
        # testing for errors related to input
        self.assertRaises(ValueError, check_input, 'apm', '4am', '9pm')
        self.assertRaises(ValueError, check_input, '5pm', 'aam', '9pm')
        self.assertRaises(ValueError, check_input, '7pm', '2am', 'apm')
        self.assertRaises(TypeError, check_input, True, '12am', '8pm')
        self.assertRaises(TypeError, check_input, '6pm', 11, '8pm')
        self.assertRaises(TypeError, check_input, '8pm', '12a', False)
        self.assertRaises(ValueError, check_input, '4pm', '1am', '8pm')
        self.assertRaises(ValueError, check_input, '5pm', '5am', '8pm')
        self.assertRaises(ValueError, check_input, '5pm', '2am', '3pm')
        self.assertRaises(ValueError, check_input, '5pm', '2am', '4am')
        self.assertRaises(ValueError, check_input, '5pm', '2am', '12am')
        self.assertRaises(ValueError, check_input, '5pm', '2am', '12pm')
        self.assertRaises(ValueError, check_input, '', '1am', '9pm')
        self.assertRaises(ValueError, check_input, '5pm', '', '8pm')
        self.assertRaises(ValueError, check_input, '6', '1am', '')
