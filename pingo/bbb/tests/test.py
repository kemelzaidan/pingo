import os
import sys
import unittest
import time

import pingo
from pingo.test import level0

class BeagleBoneBlackTest(unittest.TestCase):

    def setUp(self):
        self.board = pingo.bbb.BeagleBoneBlack()
        self.vdd_pin_number = 0
        self.digital_output_pin_number = 0
        self.digital_input_pin_number = 0
        self.total_pins = 0

    def tearDown(self):
        self.board.cleanup()


class GhostBoardBasics(BeagleBoneBlackTest, level0.BoardBasics):
    pass

class GhostBoardExceptions(BeagleBoneBlackTest, level0.BoardExceptions):
    pass


if __name__ == '__main__':
    unittest.main()
