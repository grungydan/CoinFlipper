import random

# ask user how many coin flips they wish to make
num_flips = int(input("How many times would you like to flip the coin?"))



# coin flip function
def flippit():
    
    # initialize emptly list for results
    results = []
    
    # flips counter
    flips = 0
    
    while flips < num_flips:
        if random.randint(0,1) == 0: 
            results.append("Heads")
        else:
            results.append("Tails")
        flips += 1

    print(results)
        


flippit()

# program has to flip the coin number of times prescribed
# has to result in heads or tails each flip
# has to list the results
# would be nice to tell user how many of each result were returned

        
