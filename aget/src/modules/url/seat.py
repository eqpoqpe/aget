"""
seat.py - aget

for learning communication purposes only
open-source under MIT license

Copyright (c) 2022 Ryan Martin
"""

import time
import hashlib
import hmac
import base64
from typing import (Any, Union)

def iskeyexists(d: dict, k: str):
    try:
        d[k]
    except KeyError as err:
        print("Error: not found %s key" %err)

class url:
    @staticmethod
    def public_key(s):  return s

    @staticmethod
    def ts(s):
        if s: return str(int(time.time()))

    @staticmethod
    def ttl(s):
        if s: return "200"
        else: return (lambda s: s)(s)

    @staticmethod
    def __extmap(s: list):
        return "%s=%s"%(s[0], s[1])

    @staticmethod
    def sig(p):
        iskeyexists(p, "sig")

        if not p["sig"]:
            return ""

        psig = ""
        nsig = {}

        for key in p:
            if key != "sig":
                nsig[key] = p[key]

        for index in range(len(nsig)):
            if index != len(nsig) - 1:
                psig += "%s&"
            else:
                psig += "%s"

        s = [url.__extmap([sg, p[sg]]) for sg in nsig]

        key = bytes(p["public_key"], "UTF-8")
        msg = bytes(psig%tuple(s), "UTF-8")
        digester = hmac.new(key, msg, hashlib.sha1)
        sig = base64.urlsafe_b64encode(digester.digest())

        p["sig"]= str(sig, "UTF-8")

class urli:
    interface = {
        "public_key": lambda s: s,
        "ts": lambda s: str(int(time.time())),
        "ttl": url.ttl,
    }

class urls:

    @staticmethod
    def sval(s: Union[bool, str], k: str=False) -> str:
        
        """ check value """
        if type(s) == bool and s:
            return urli.interface[k](s)
        return s