a = 7823        # this is a global variable, which is accessible anywhere

def corn():
    print(a)

    b = 3287
    print(b)    # variable declared inside a funcion

def funge():
    print(a)
    #print(b)    # we can't use this variable 'b' anywhere else but the function 'corn()'

corn()
funge()