"""
url.py - aget

for learning communication purposes only
open-source under MIT license

Copyright (c) 2022 Ryan Martin
"""

from typing import Union

class url:

    @staticmethod
    def __extmap(s: list):
        return "%s=%s"%(s[0], s[1])

    @staticmethod
    def merge(d: str, p: Union[dict, str]) -> str:
        purl = ""

        if type(p) == dict:
            for index in range(len(p)):
                if index != len(p) - 1: purl += "%s&"
                else:   purl += "%s"

            s = [url.__extmap([sg, p[sg]]) for sg in p]

            return "%s?%s"%(d, purl%tuple(s))

        elif type(p) == str:
            ...
