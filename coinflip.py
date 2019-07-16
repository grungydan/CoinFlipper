import random

# ask user how many coin flips they wish to make
num_flips = int(input("How many times would you like to flip the coin?"))



# coin flip function
def flippit():

    #initialize empty list of results
    results = []
    
    # flips counter
    flips = 0

    # while loop to continue flipping until num_flips reached
    while flips < num_flips:
        toss = random.randint(0,1)
        results.append(toss)
        flips += 1
    return(results)





