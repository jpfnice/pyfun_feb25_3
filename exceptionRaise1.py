

def isprime(number):
    if not isinstance(number, int):
        # e=ValueError("The parameter given to isNumber must be an int!")
        # raise e
        raise ValueError("The parameter given to isNumber must be an int!")
    if number <= 0:
        return False
    for divisor in range(2,number):
        if number % divisor == 0:
            return False
    return True
    

values=[12,13,"ABC", 14,15,3.4, -5,23,24,27]
for e in values:
    try:
        print(e,"->", isprime(e))
    except ValueError as ex:
        print("There is a problem with the value", e)