"""
param.py - aget

for learning communication purposes only
open-source under MIT license

Copyright (c) 2022 Ryan Martin
"""

import re
from typing import (Any)
from .seat import (url, urls)


class param:

    @staticmethod
    def parse(config: Any) -> tuple:
        
        """ return a tuple(path, parameters) """
        return ((lambda s: "%s://%s%s" %(s[0], s[1], s[2]))([gs for gs in re.sub(r"@.*$", "", str(config)).split(':')]), \
            re.compile("@(.+)").findall(str(config))[0])

        # print(config)

    @staticmethod
    def fill(param: dict) -> str:
        sig = False

        for key in param:
            if key != "sig":
                param[key] = urls.sval(param[key], key)
            else:
                sig = True

        if sig:
            url.sig(param)

        return param

class fill:
    def __init__(self, p: dict) -> None:
        self.__param = p

    def mkparam(self) -> str:   return ""