import json
import time
from modules import Config
from modules import (param, fill)

config = Config(Config.rconf("./config.ci.json"))
parameters = param.parse(config)[1]

dat = json.loads(parameters)
dat = param.fill(dat)
# result = fill(dat).tostr()

# print(result)

# print(urllib.parse.quote("GHETq6Tvivz10hr++znDO/Jew7E="))