"""
Created on 20 Dec 2025

@author: Bruno Beloff (bbeloff@me.com)

HTTPResponse exception handler
"""

from httpx import Response


# ----------------------------------------------------------------------------------------------------------------

class HTTPResponseException(RuntimeError):
    """
    HTTPResponse exception handler
    """

    @classmethod
    def check(cls, response: Response, *expected_response_codes):
        if response.status_code not in expected_response_codes:
            raise cls.construct(response)


    @classmethod
    def construct(cls, response: Response):
        return cls(response.status_code, response.reason_phrase)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, status_code: int, reason_phrase: str):
        self.__status_code = status_code
        self.__reason_phrase = reason_phrase


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def status_code(self):
        return self.__status_code


    @property
    def reason_phrase(self):
        return self.__reason_phrase


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return f'HTTPResponse: {self.status_code}: {self.reason_phrase}'


