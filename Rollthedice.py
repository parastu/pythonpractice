import random
min = 1
max = 6
roll_again = "yes"
while roll_again == "yes":
    print ("Rolling the dice...")
    print (random.randint(min,max))
    print (random.randint(min,max))
    roll_again = input("Take another chance?")
    
