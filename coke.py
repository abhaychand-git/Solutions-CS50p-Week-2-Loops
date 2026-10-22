amount_due=50

while amount_due < 0:
    print ("Amount Due:", amount_due)
    amount= int (input ("Insert Coin:"))
        if amount==25:
        amount_due-=amount
    elif amount==10:
        amount_due-=amount
    elif amount==5:
        amount_due-=amount
