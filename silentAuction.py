#-------------------------------------------------------------------------------
# Name:        silentAuction
# Purpose:     to carry out a silent auction
# Version 1 -  base program
# Author:      May Robertson
# Created:     08/02/2019

def get_float(q):
    f=int(input(q))
    return f





highestBid=0
bidCount=0
name=""
CLB=[]
names=[]
bids=[]

reservePrice=get_float("What is the reserve price?")
while name.upper()!="F":
    print("Highest bid so far is:",highestBid)
    name=input("What's your name? If you are finished bidding please enter F")
    if name.upper() != "F":
        bid=get_float("Please enter the amount you want to pay")
        if bid>highestBid:
            highestBid=bid
            bids.append(bid)
            names.append(name)
            bidCount+=1
        else:
            print("Sorry "+name+" You'll need to make another, higher bid.")
        if highestBid>=reservePrice:
            print("Auction won",name,"at",bids[bidCount-1])
        else:
            print("Auction did not meet the reserve price")

        for i in range (bidCount):
            print(names[i],bids[i])
        
