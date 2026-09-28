blah = [1, 7, 19, 22]

for i in range(len(blah)):
    if blah[i] == 0:
        print ("Zero")
    elif blah[i] == 1:
        print ("Odd")
    elif blah[i] % 2 == 0:
        print ("Even")
    else:
        print ("Odd")
