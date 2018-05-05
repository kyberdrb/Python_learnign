magicNumber = 26

for n in range(101):
    if n is magicNumber:
        print(n, "is the magic number!")
        break
    else:
        print(n)

"""
this is
a multiline comment
"""

# this is a singleline comment

print()

print("Bucky" + "3")
#print("Bucky" + 3)  # error: python can't add an integer to a string
print(3, "Bucky")

print()

# Print every number up to 100 that can be divided by 4
for i in range(101):
    # following two conditions do the same thing
    if i % 4 is 0:
        if (i % 4) == 0:
            print(i)