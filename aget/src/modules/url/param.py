"""
param.py - aget

for learning communication purposes only
open-source under MIT license

Copyright (c) 2022 Ryan Martin
"""

from curses.ascii import isctrl
import re
from typing import (Any)
from .seat import (url, urls)


class param:

    @staticmethod
    def parse(config: Any) -> tuple:
        return ((lambda s: "%s://%s%s" %(s[0], s[1], s[2]))([gs for gs in re.sub(r"@.*$", "", str(config)).split(':')]), \
            re.compile("@(.+)").findall(str(config))[0])

    @staticmethod
    def fill(param: dict) -> str:
        for key in param:
            if key != "sig":
                param[key] = urls.sval(param[key], key)

        url.sig(param)

        return param

class fill:
    def __init__(self, p: dict) -> None:
        self.__param = p

    def mkparam(self) -> str:   return ""