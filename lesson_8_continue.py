numbersTaken = [2, 5, 12, 33, 17]

print("Here are the numbers that are still availible:")
for n in range(1, 20):
    if n in numbersTaken:
        #print(n, "\texcluded")
        continue
    print(n)