

values=["Geneva", "Nyon", "Versoix", "Bern", "Gland"]

try:
    index=input("Enter an int in the range [0,4]: ")
    index=int(index)

    print(f"At position {index} there is the city {values[index]}")
except:
    print("An exception is raised")
    
print("The end")