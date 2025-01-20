import art

print(art.logo)
auction = {}
new_bidder = True

# def compare_bids(bid):
#     highest_bid = 0
#     winner = ""
#     for key in auction:
#         bid_amount = auction[key]
#         if bid_amount>highest_bid:
#             highest_bid = bid_amount
#             winner = key

    # print(f"the winner is {winner} with bid of {highest_bid}$ ")
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
while new_bidder:

    name = input("name of the bidder:- \n")
    bidding_price = int(input("please enter your bid:- \n"))
    auction[name] = bidding_price
    new_user = input("new bidder needed? yes/no :- \n").lower()
    if new_user == "yes":
        print("\n"*50)
    elif new_user == "no":
        new_bidder = False
        # compare_bids(name)
        winner_auc = max(auction, key=auction.get)
        print(f"the winner is {winner_auc} with bid of {bidding_price}$ ")
        print(auction)



# TODO-4: Compare bids in dictionary


