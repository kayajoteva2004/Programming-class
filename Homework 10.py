# Secret Auction Game

bids = {}
bidding_finished = False

# Handle stopping of bidders =>
while not bidding_finished:
    name = input("What is your name? ")
    bid = int(input("How much you are bidding? $$$"))
    bids[name] = bid

    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if should_continue == "no":
        bidding_finished = True
# make it secret so the next entry does not show the previous one.
    else:
        print("\n" * 100)

highest_bid = 0
winner = ""

for bidder in bids:
    bid_amount = bids[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder

print(f"The winner is {winner} with a bid of ${highest_bid}")
