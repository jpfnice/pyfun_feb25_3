
import json

myfile=open("data.json")

adict=json.load(myfile)

myfile.close()

print(adict["homeTown"])
print(adict["members"][0]["age"])
print(adict["members"][1]["name"])

