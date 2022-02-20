import json
from modules import Config
from modules import (param, merge)

config = Config(Config.rconf("./config.ci.json"))
url = param.parse(config)[0]
parameters = param.parse(config)[1]

dat = json.loads(parameters)
par = param.fill(dat)

print(merge.merge(url, par))