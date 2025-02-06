
# afile=open("data.txt")

# for line in afile:
#     print(line)
    
# afile.close()

# When the with block is left, the file is closed
with open("data.txt") as afile:
    for line in afile:
        print(line)
