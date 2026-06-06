# The goal is to build a blind auction program.

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary



import art
print(art.logo)
def find_highest_bidder(bidding_dict):
    winner=""
    highest_bid=0
    
    for i in bidding_dict:
        amount=bidding_dict[i]
        if amount > highest_bid:
            highest_bid = amount
            winner=i
    print(f"the winner is {winner} with a bid of ${highest_bid}")
  # for direct max value u can use formula = max(dict,key=dict.get)

dict={}
bidding=True
while bidding :
     x=input("What is your name?: ")
     y=int(input("What is your bid?: $ "))
     dict[x]=y
     z=input("Are there any other bidders? Type 'yes or no").lower()
     if z == "no":
         bidding = False
         find_highest_bidder(dict)
     elif z == "yes":
         print("\n"*30)


