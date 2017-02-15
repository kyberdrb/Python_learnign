# "Dictionary" is a data structure, which stores key-value pairs, just like HashMap in Java

classmates = {"Tony":"cool but smells", "Emma":"sits behind me", "Lucy":"asks too many questions"}

print(classmates)
print(classmates['Emma'])

print()

# we can loop through dictionary with for-each loop
# the items are printed RANDOMLY!
for k,v in classmates.items():
    print(k + " " + v)