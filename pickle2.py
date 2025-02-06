
import pickle



with open("newfile.pick", "rb") as afile:
    adict=pickle.load(afile)
    
print(adict)