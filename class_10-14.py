# number = int(input("Enter a number: "))
# print(number)

# If you want this program to be able to handle "ten", you need to work in 
# exception handling into your code. Any code that we want protected, we put 
# inside something called try

# has_error = True

# You would intuitiveley type this out as "while has_error == True" but 
# you can just do it this way because its a boolean
#while has_error:
   # try:
       # number = int(input("Enter a number: "))
       # print(number)
    #except ValueError:
       # print("Invalid entry. Please try again with a numberical positive entry.")
       # continue
   # else:
       # has_error = False
   # finally:
        #print("Got through it!")

# There is a question on the exam that deals with continue or break

# When using the debugger, if you step over it will just skip the line of
# code. If you step into a function, it will show each line of code in the 
# function as well. 

#has_error = True

#while has_error:
    #try:
        #number = int(input("Enter a number: "))
        #print(number)

        #has_error = False

    #except ValueError:
        #print("Invalid entry. Please try again with a numberical positive entry.")
    #except KeyboardInterrupt:
        #print("You you stopped the program")
        #break
    #except:
        #print("You got some rando error")
        #break

def withdraw(amount, balance):
    if amount > balance:
        raise Exception("Insufficient Funds")
    return balance - amount