import random

# ask user how many coin flips they wish to make
num_flips = int(input("How many times would you like to flip the coin? "))



# coin flip function
def flippit():
    
    # initialize emptly list for results
    results = []
    
    # counters
    flips = 0
    heads = 0
    tails = 0

    while flips < num_flips:
        if random.randint(0,1) == 0: 
            results.append("Heads")
            heads += 1
        else:
            results.append("Tails")
            tails += 1
        flips += 1

    print("Heads came up {} times, and Tails came up {} times.".format(heads, tails))
    print("The individual results in order were {}.".format(results))
        
flippit()        
