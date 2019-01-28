# find multiples of 3 and 5
# sum

# make a function with an input x

# find all values less than x which are multiples of 3 and 5
    # use a count up
    # check for 3
    # save into array
    # check for 5
    # save into array
    
# add all the numbers together
# print sum

# not working because Python can't divide integers

def multiples(total):
    # counting variable
    y = 0
    # count up until you reach x
    while y < total:

        y += 1
        print y
              
        if isinstance(y / 3.0, int):
            print y, "is a multiple of 3"
            
        elif isinstance(y / 5.0, int):
            print y, "Is a multiple of 5"
        else:
            print y, "is not a multiple of 3 or 5"
        

## find out how to use this variable as a function parameter, scope?  
##x = raw_input("Enter an integer: ")

multiples(100)

##y = 2
##print isinstance(3/2, int)

##    print y, "is a multiple of 3"
##else:
##    print y, "is not a multiple of 3"
