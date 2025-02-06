

values=["Geneva", "Nyon", "Versoix", "Bern", "Gland"]

while True:
    try:
        index=input("Enter an int in the range [0,4]: ")
        index=int(index)
        print(f"At position {index} there is the city {values[index]}")
        break
    
    except ValueError as ex:
        print("A Value Error exception has been raised !")
        print("The message is", ex)
    except IndexError as ex:# The block that do follow is executed if an 
         #  IndexError exception is raised in the try block
        print("A Index Error exception has been raised !")
        print("The message is", ex)

    
print("The end")