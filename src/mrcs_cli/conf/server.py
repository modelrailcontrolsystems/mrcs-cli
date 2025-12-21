"""
Created on 6 Dec 2025

@author: Bruno Beloff (bbeloff@me.com)

The MRCS local web server base URL configuration

{
    "host": "127.0.0.1",
    "port": 8000,
    "is_secure": false
}

https://en.wikipedia.org/wiki/URL
"""

from collections import OrderedDict

from mrcs_core.data.json import PersistentJSONable


# --------------------------------------------------------------------------------------------------------------------

class Server(PersistentJSONable):
    """
    classdocs
    """

    __FILENAME = "server_conf.json"

    @classmethod
    def persistence_location(cls):
        return cls.conf_dir(), cls.__FILENAME


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict, skeleton=False):
        if not jdict:
            return None

        host = jdict.get('host')
        port = jdict.get('port')
        is_secure = jdict.get('is_secure')

        return cls(host, port, is_secure)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, host: str, port: int, is_secure: bool):
        super().__init__()

        self.__host = host
        self.__port = port
        self.__is_secure = is_secure


    # ----------------------------------------------------------------------------------------------------------------

    def base_url(self):
        scheme = 'https' if self.is_secure else 'http'
        port = '' if self.port == 80 else ':' + str(self.__port)

        return f'{scheme}://{self.host}{port}/'


    def url(self, path):
        return self.base_url() + path


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self, **kwargs):
        jdict = OrderedDict()

        jdict['host'] = self.host
        jdict['port'] = self.port
        jdict['is_secure'] = self.is_secure

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def host(self):
        return self.__host


    @property
    def port(self):
        return self.__port


    @property
    def is_secure(self):
        return self.__is_secure


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return (f'Server:{{host:{self.host}, port:{self.port}, is_secure:{self.is_secure}, '
                f'last_modified:{self.last_modified}}}')
