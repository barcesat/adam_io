import base64
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from typing import Dict, Optional
from .utils import URI


class Requestor:
    def __init__(self, ip: str, username: str, password: str):
        """
        For now no unauthorized requests are possible

        :param ip: ADAM ip
        :param username: ADAM username
        :param password: ADAM password
        """
        auth_str = f"{username}:{password}"
        encoded_auth_str = base64.b64encode(auth_str.encode('ascii')).decode('utf-8')
        self.headers = {"Content-Type": "application/x-www-form-urlencoded",
                        "Authorization": "Basic " + encoded_auth_str}
        self.base_url = f"http://{ip}"

    def d_input(self, input_channel_id: Optional[int] = None):
        """
        if the requests digital output index is out of bounds,
        request returns status code 501.

        :param input_channel_id: single input is requested, none returns all digital inputs
        :return: ADAM response, xml response with status code/message
        """
        if input_channel_id:
            input_channel_id = "/" + str(input_channel_id)
            url = self.base_url + URI.DIGITAL_INPUT + input_channel_id + URI.VALUE
        else:
            url = self.base_url + URI.DIGITAL_INPUT + URI.ALL + URI.VALUE
        request = Request(url, headers=self.headers)
        response = urlopen(request)
        return response.read().decode('utf8')

    def d_output(self, data: Optional[Dict[str, int]] = None):
        """
        if the requests digital output index is out of bounds,
        request returns status code 501.

        :param data: DigitalOutput object converted to dictionary as {"DO1":1,...}
        :return: ADAM response, xml response with status code/message
        """
        url = self.base_url + URI.DIGITAL_OUTPUT + URI.ALL + URI.VALUE
        # print(url)
        if data:
            params = urlencode(data).encode('utf-8')
            print(params)
            request = Request(url, data=params, headers=self.headers)
            print(request.header_items())
        else:
            request = Request(url, headers=self.headers)

        response = urlopen(request)
        return response.read().decode('utf8')

    def a_input(self, input_channel_id: Optional[int] = None):
        """
        if the requests analog output index is out of bounds,
        request returns status code 501.

        :param input_channel_id: single input is requested, none returns all analog inputs
        :return: ADAM response, xml response with status code/message
        """
        if input_channel_id:
            input_channel_id = "/" + str(input_channel_id)
            url = self.base_url + URI.ANALOG_INPUT + input_channel_id + URI.VALUE
        else:
            url = self.base_url + URI.ANALOG_INPUT + URI.ALL + URI.VALUE
        request = Request(url, headers=self.headers)
        response = urlopen(request)
        return response.read().decode('utf8')

    def a_output(self, data: Optional[Dict[str, int]] = None):
        """
        if the requests analog output index is out of bounds,
        request returns status code 501.

        :param data: ANALOGOutput object converted to dictionary as {"AO1":1,...}
        :return: ADAM response, xml response with status code/message
        """
        url = self.base_url + URI.ANALOG_OUTPUT + URI.ALL + URI.VALUE
        print(url)
        if data:
            params = urlencode(data).encode('utf-8')
            print("params: ",params)
            request = Request(url, data=params, headers=self.headers)
            print("Request: ",request.header_items)
        else:
            request = Request(url, headers=self.headers)
        
        response = urlopen(request)
        print(response.read().decode('utf8'))
        return response.read().decode('utf8')