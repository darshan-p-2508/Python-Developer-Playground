# First-price sealed-bid auction (FPSBA)
# a.k.a Blind Auction

# print("Hello")
# print("\n" * 100)   # this scrolls the screen to 100th next line to make the previous details disappear


bids = {}

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with  bid of ${highest_bid}")

continue_bidding = True

while continue_bidding:
    name = input("What is your name? ")
    bid_amount = int(input("what amount would you like to bid? $"))
    bids[name] = bid_amount
    should_continue = input("Are there ny other bidders?\nType 'Yes' or 'No': ").lower()

    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 100)

