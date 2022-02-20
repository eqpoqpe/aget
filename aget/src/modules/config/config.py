"""
config.py - aget

Copyright (c) 2022 Ryan Martin
"""

from importlib.resources import path
import json
import os
from symtable import Function
import sys
import types
from typing import (Any, Union, NoReturn, overload)
from pathlib import Path

# default config path to '$WORKING_DIR/config.ci.json'

class Config:

    """
    return str format with "protocl:domain:path@parameter1"
    
    saved the order of parameters
    """
    def __init__(self, d: Union[dict, int], handle: Any=None) -> None:
        __apiconfig = "apiconfig"
        __dynamic = "dynamic"
        __static = "static"
        __protocol = "protocol"
        __domain = "domain"
        __path = "path"
        __parameter = "parameter"

        self.__plugin = []
        self.__param = {}

        """
        added key existing check

        dynamic -> list(array)
        static  -> dict
        """
        try:
            d[__apiconfig]
            self.__keycheck(d, [__protocol, __domain, __path])
            self.__param = d
        except KeyError as err:
            print("Error: not found key %s" %err)

    def __setattr__(self, __name: str, __value: Any) -> None:
        self.__dict__[__name] = __value

    def __str__(self) -> str:
        apiconfig = self.__param["apiconfig"]

        return "%s:%s:%s@%s" %(
            apiconfig["protocol"],
            apiconfig["domain"],
            apiconfig["path"],
            json.dumps(apiconfig["parameter1"])
            )

    def __keycheck(self, d: dict, kks: Union[list, str]) -> NoReturn:
        ks = kks
        
        for key in kks:
            try:
                d[key]
            except:
                d["apiconfig"][key]

    @overload
    def Info(self):
        ...

    @overload
    def Info(self, s: str):
        ...

    @staticmethod
    def rconf(filepath: Union[Path, str]) -> Any:
        if os.path.isfile(filepath):
            with open(filepath, "r") as fp:
                c = json.load(fp)

                return c
