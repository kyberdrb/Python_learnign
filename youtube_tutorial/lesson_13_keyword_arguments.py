def dumb_sentence(name='Bucky', action='ate', item='tuna'):
    print(name, action, item)

dumb_sentence()

# by DEFAULT, arguments are passed to the function in order, they are declared
dumb_sentence("Sally", "sings", "gently")

# we can pass the arguments to the function in different order
dumb_sentence(item="sausage")
dumb_sentence(item="TV", action="watches")