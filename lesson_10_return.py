def allowed_dating_age(my_age):
    girls_age = my_age / 2 + 7
    return girls_age

def print_allowed_age(name, your_age):
    print(name + " can date girls", allowed_dating_age(your_age), "or older")

print_allowed_age("Bucky", 27)
print_allowed_age("Creepy Joe", 49)

print()

for age in range(15, 61):
    print(age, "\t", allowed_dating_age(age))