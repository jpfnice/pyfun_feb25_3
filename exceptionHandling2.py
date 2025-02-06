

values=["Geneva", "Nyon", "Versoix", "Bern", "Gland"]

try:
    index=input("Enter an int in the range [0,4]: ")
    index=int(index)

    print(f"At position {index} there is the city {values[index]}")
except ValueError as ex:
    print("A Value Error exception has been raised !")
    print("The message is", ex)
except IndexError as ex:
    print("A Index Error exception has been raised !")
    print("The message is", ex)
    
print("The end")