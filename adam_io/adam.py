"""
ADAM 6050-D
===========
Main ADAM module to make the requests for input and output operations
"""

from xml.etree import ElementTree

from .digital_io import DigitalInput, DigitalOutput
from .analog_io import AnalogInput, AnalogOutput
from .requestor import Requestor
from .utils import valid_ipv4
from typing import Optional


class Adam6050D:
    """
    Only the ADAM6050D module is supported.
    """

    DO_COUNT = 6
    DI_COUNT = 12

    def __init__(self, ip: str, username: str, password: str):
        """
        Username and password should already be setup from APEX(?)
        :param ip: ip address of ADAM, should be of the form 0.0.0.0
        :param username: username for ADAM
        :param password: password for ADAM
        """
        if not valid_ipv4(ip):
            raise Exception("not a valid ip address ", ip)
        self.requestor = Requestor(ip, username, password)

        # make an initial request
        # input_response = self.input()
        # print("Initialized " + input_response.name)

    def output(self, digital_output: Optional[DigitalOutput] = None):
        """
        This prepares the data and sends it over to ADAM.

        :param digital_output: DigitalOutput, if the digital_output is None, read the values, not set them.
        :return: True for success, raises an exception if unsuccessful
        """

        # set the value(s) of the current state to that of input's
        if digital_output:
            current_state = self.requestor.d_output()
            current_do = DigitalOutput(xml_string=current_state)
            for key, val in digital_output:
                key = int(key.replace("DO", ""))
                if val is not None:
                    current_do[key] = digital_output[key]
            response = self.requestor.d_output(current_do.as_dict())
            root = ElementTree.fromstring(response)
            status = root.attrib['status']
            if status != "OK":
                raise Exception("Couldn't update output: ", status)
            return True
        else:
            response = self.requestor.d_output(digital_output)
            return DigitalOutput(xml_string=response)

    def input(self, digital_input_id: Optional[int] = None):

        """
        Read the values of the digital inputs

        :param digital_input_id: DIx if the digital_input_id is None, read the all values
        :return: ADAM response
        """
        response = self.requestor.input(digital_input_id)
        return DigitalInput(response)

    def on(self):
        """
        All digital outputs to HIGH
        """
        do = DigitalOutput(array=[1] * Adam6050D.DO_COUNT)
        # this is also acceptable
        # do.array([1, 1, 1, 1, 1, 1])
        # as well as this
        # do[0] = 1
        # do[1] = 1
        # do[2] = 1
        # do[3] = 1
        # do[4] = 1
        # do[5] = 1
        return self.output(do)

    def off(self):
        """
        All digital outputs to LOW
        """
        do = DigitalOutput(array=[0] * Adam6050D.DO_COUNT)
        return self.output(do)

class Adam6024D:
    """
    Only the ADAM6240D module is supported.
    """

    DO_COUNT = 2
    DI_COUNT = 2
    AO_COUNT = 2
    AI_COUNT = 6


    def __init__(self, ip: str, username: str, password: str):
        """
        Username and password should already be setup from APEX(?)
        :param ip: ip address of ADAM, should be of the form 0.0.0.0
        :param username: username for ADAM
        :param password: password for ADAM
        """
        if not valid_ipv4(ip):
            raise Exception("not a valid ip address ", ip)
        self.requestor = Requestor(ip, username, password)

        # make an initial request
        # input_response = self.input()
        # print("Initialized " + input_response.name)

    def d_output(self, digital_output: Optional[DigitalOutput] = None):
        """
        This prepares the data and sends it over to ADAM.

        :param digital_output: DigitalOutput, if the digital_output is None, read the values, not set them.
        :return: True for success, raises an exception if unsuccessful
        """

        # set the value(s) of the current state to that of input's
        if digital_output:
            current_state = self.requestor.d_output()
            current_do = DigitalOutput(xml_string=current_state)
            for key, val in digital_output:
                key = int(key.replace("DO", ""))
                if val is not None:
                    current_do[key] = digital_output[key]
            print(current_do)
            response = self.requestor.d_output(current_do.as_dict())
            root = ElementTree.fromstring(response)
            status = root.attrib['status']
            if status != "OK":
                raise Exception("Couldn't update output: ", status)
            return True
        else:
            response = self.requestor.d_output(digital_output)
            return DigitalOutput(xml_string=response)

    def d_input(self, digital_input_id: Optional[int] = None):

        """
        Read the values of the digital inputs

        :param digital_input_id: DIx if the digital_input_id is None, read the all values
        :return: ADAM response
        """
        response = self.requestor.d_input(digital_input_id)
        return DigitalInput(response)

    def on(self):
        """
        All digital outputs to HIGH
        """
        do = DigitalOutput(array=[1] * Adam6024D.DO_COUNT)
        # this is also acceptable
        # do.array([1, 1, 1, 1, 1, 1])
        # as well as this
        # do[0] = 1
        # do[1] = 1
        return self.d_output(do)

    def off(self):
        """
        All digital outputs to LOW
        """
        do = DigitalOutput(array=[0] * Adam6024D.DO_COUNT)
        return self.d_output(do)

    def a_output(self, analog_output: Optional[AnalogOutput] = None):
        """
        This prepares the data and sends it over to ADAM.

        :param analog_output: AnalogOutput, if the analog_output is None, read the values, not set them.
        :return: True for success, raises an exception if unsuccessful
        """

        # set the value(s) of the current state to that of input's
        if analog_output:
            current_state = self.requestor.a_output()
            current_ao = AnalogOutput(xml_string=current_state)
            # print(current_ao)
            for key, val in analog_output:
                key = int(key.replace("AO", ""))
                if val is not None:
                    current_ao[key] = analog_output[key]
            # print(current_ao)
            response = self.requestor.a_output(current_ao.as_dict())
            root = ElementTree.fromstring(response)
            status = root.attrib['status']
            if status != "OK":
                raise Exception("Couldn't update output: ", status)
            return True
        else:
            response = self.requestor.a_output(analog_output)
            return AnalogOutput(xml_string=response)

    def a_input(self, analog_input_id: Optional[int] = None):

        """
        Read the values of the analog inputs

        :param analog_input_id: DIx if the analog_input_id is None, read the all values
        :return: ADAM response
        """
        response = self.requestor.a_input(analog_input_id)
        return AnalogInput(response)
