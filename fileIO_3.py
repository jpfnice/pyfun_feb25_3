
# When the with block is left, the file is closed
# "w" "a" "r" "w+" "r+" "a+" 
with open("newfile.txt", "a") as afile:
    afile.write("Some text\n")
    afile.write("Another text\n")
    print("Hello World", file=afile)
    print("The end", file=afile)