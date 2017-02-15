# A "Set" is a list that can't have duplicates in it

groceries = {'cereal', 'milk', 'starcrunch', 'beer', 'duck type', 'lotion', 'beer'}
print(groceries)    # beer is only once

if 'milk' in groceries:
    print("You already have milk hoss!")
else:
    print("Oh yea, you have milk!")