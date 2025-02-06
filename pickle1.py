
import pickle

test={
  "name": "Eternal Flame",
  "age": 1000000,
  "secretIdentity": "Unknown",
  "powers": [
    "Immortality",
    "Heat Immunity",
    "Inferno",
    "Teleportation",
    "Interdimensional travel"
  ]
}

with open("newfile.pick", "wb") as afile:
    pickle.dump(test, afile)
    