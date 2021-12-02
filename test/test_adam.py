import unittest
from unittest.mock import Mock

from adam_io.adam import Adam6050D
from adam_io.digital_io import DigitalOutput


class AdamTest(unittest.TestCase):

    def setUp(self) -> None:
        self.adam = Adam6050D('192.168.1.110', 'root', '00000000')
        self.adam.output = 0

    def test_output(self):
        self.assertTrue(self.adam.output(DigitalOutput()))
