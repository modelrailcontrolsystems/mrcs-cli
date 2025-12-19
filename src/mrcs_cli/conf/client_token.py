"""
Created on 19 Dec 2025

@author: Bruno Beloff (bbeloff@me.com)

A JSON Web Token (JWT) carrying scopes

https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/#verify-the-scopes
"""

from collections import OrderedDict

from mrcs_core.data.json import PersistentJSONable

from mrcs_core.security.token import AccessToken, JWT


# --------------------------------------------------------------------------------------------------------------------

class ClientJWT(JWT, PersistentJSONable):
    """
    A locally-persistent JSON Web Token (JWT)
    """

    __FILENAME = "token.json"

    @classmethod
    def persistence_location(cls):
        return cls.conf_dir(), cls.__FILENAME


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict):
        if not jdict:
            return None

        access = AccessToken(jdict.get('access_token'), None)
        token_type = jdict.get('token_type')

        return cls(access, token_type)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, access: AccessToken, token_type: str = JWT.TOKEN_TYPE):
        super().__init__(access, token_type)


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self, expiry=None):
        jdict = OrderedDict()

        jdict['access_token'] = self.access.data
        jdict['token_type'] = self.token_type

        return jdict
