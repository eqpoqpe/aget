"""
aget.py - aget

for learning communication purposes only
open-source under MIT license

Copyright (c) 2022 Ryan Martin
"""

import requests
import json
from modules import (Config, url)
from typing import (Union)

# result = requests.get("http://t.weather.sojson.com/api/weather/city/101120901", auth=("user", "pass"))

# print(json.dumps(result.json(), ensure_ascii=False, indent=4))

# with open("request_data.json", "w", encoding="utf8") as fp:
#     json.dump(result.json(), fp, ensure_ascii=False, indent=4)


def info():
    ...

class aget:
    ...

def URL(maker, param: Config) -> Union[str, bool]:
    return param

def main():
    _url = URL(url, Config(Config.rconf("./config.ci.json")))
    print(_url)

if __name__ == "__main__":
    main()