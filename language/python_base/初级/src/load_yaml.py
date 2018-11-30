import yaml
import sys
stream = open('config.yaml','r')
data = yaml.load(stream)
print(data)
print(data["SIT"])
