from json import load
from pprint import pprint

with open('resources') as f:
    data = json.load(f)
pprint(data)
