"""
Created on 18 Dec 2025

@author: Bruno Beloff (bbeloff@me.com)

The MRCS local web server base URL configuration

{
    "username": "127.0.0.1",
    "password": 8000,
    "is_secure": false
}

https://en.wikipedia.org/wiki/URL
"""

from collections import OrderedDict

from mrcs_core.data.json import PersistentJSONable


# --------------------------------------------------------------------------------------------------------------------

class Credentials(PersistentJSONable):
    """
    classdocs
    """

    __FILENAME = "credentials.json"

    @classmethod
    def persistence_location(cls):
        return cls.conf_dir(), cls.__FILENAME


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict, skeleton=False):
        if not jdict:
            return None

        username = jdict.get('username')

        return cls(username, None)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, username: str, password: str | None):
        super().__init__()

        self.__username = username
        self.__password = password


    # ----------------------------------------------------------------------------------------------------------------

    def as_form(self, **kwargs):
        jdict = OrderedDict()

        jdict['grant_type'] = 'password'
        jdict['username'] = self.username
        jdict['password'] = self.password

        return jdict


    def as_json(self, **kwargs):
        jdict = OrderedDict()

        jdict['username'] = self.username

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def username(self):
        return self.__username


    @property
    def password(self):
        return self.__password


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return f'Credentials:{{username:{self.username}, password:{self.password}, last_modified:{self.last_modified}}}'
