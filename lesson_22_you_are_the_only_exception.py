# # tuna = int(input("What's your favourite number?\n"))
# print(tuna)

while True:
    try:
       number = int(input("What's your favourite number?\n"))
       print(18/number)
       break
    except ValueError:  # user entered bad input
        print("I expect a number!")
    except ZeroDivisionError:
        print("Can't divide by 0!")
    except: # all other exceptions
        break
    finally:
        print("loop complete")