
import json

# from json import load, loads


# from math import *
# print(sqrt(5), cos(3.4), sin(6.7))

myfile=open("data.json")

adict=json.load(myfile)

myfile.close()

print(adict["homeTown"])
print(adict["members"][0]["age"])
print(adict["members"][1]["name"])

