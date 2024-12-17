def highest_bidder(dict):      
    max_score = 0
    for bidder in dict:
        if dict[bidder] > max_score:
            max_score = dict[bidder]
    print(f"The winner is {bidder}, with the amount ${max_score}")



dict = {} 
next_bid = True

while next_bid:
    name = input("What is your Name?: ")
    price = int(input("What is your bid price?: $"))
    
    dict[name] = price
    
    
    repeat = input("Type yes to continue, Type No to end the bid").lower()

    if repeat == "no":
        next_bid = False
        highest_bidder(dict)
    elif repeat == "yes":
        print("\n" *5)