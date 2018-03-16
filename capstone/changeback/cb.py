#!python

'''
CHANGE BACK

This program takes a purchase total and some cash. It
returns the number of bills and coins needed for change.

- Returns minimum amount of bills and coins.

Algorithm:

    cash_back = cash_tendered - purchase_price
    pennies = cash_back % 5 cents / 1 cent
    nickels = cash_back % 10 cents / 5 cents
    dimes = cash_back % 10 cents / 10 cents
    denomination count = cash_back % next denomination / denomination
    if no more denominations
        denomination_count += int(cash_back/denomination)
    until sum == cash_back or no more denominations

    pennies = cash_back % 5
    nickels = cash_back - pennies % 10 / 5 unless
        cash_back - pennies - nickels * 5 % 25 is not an integer
        in that case, skip nickels

    How about getting cents and take out 50c, 25c, 10c, 5c?
    Then, switch to 1,2,5 x 10**n case
'''


PENNY = ('1c', 1)
NICKEL = ('5c', 5)
DIME = ('10c', 10)
QUARTER = ('25c', 25)
FIFTY_CENT_PIECE = ('50c', 50)
DOLLAR_BILL = ('$1', 100)
TWO_DOLLAR_BILL = ('$2', 200)
FIVE_DOLLAR_BILL = ('$5', 500)
TEN_DOLLAR_BILL = ('$10', 1000)
TWENTY_DOLLAR_BILL = ('$20', 2000)

DENOMINATIONS = [PENNY, NICKEL, DIME, QUARTER, FIFTY_CENT_PIECE,\
        DOLLAR_BILL, FIVE_DOLLAR_BILL, TEN_DOLLAR_BILL,\
        TWENTY_DOLLAR_BILL]

class Cash():
    ''' holds an amount of money partitioned by denominations '''

    def __init__(self, amount=0):
        self.bank = {}
        for i in range(len(DENOMINATIONS) - 1):
            symbol, face_value = DENOMINATIONS[i]
            _, next_face_value = DENOMINATIONS[i + 1]
            self.bank[symbol] = \
                    int(amount % next_face_value / face_value)
            amount -= self.bank[symbol]
            if amount <= 0:
                break
        else:
            symbol, face_value =\
                    DENOMINATIONS[len(DENOMINATIONS) - 1]
            self.bank[symbol] = int(amount / face_value)
        for i in range(len(self.bank), len(DENOMINATIONS)):
            self.bank[i] = 0

    def __str__(self):
        total = 0
        header = ''
        counts = ''
        amounts = ''
        for symbol, face_value in DENOMINATIONS:
            header += symbol + '\t'
            count = self.bank[symbol] 
            counts += str(count) + '\t'
            amount = (self.bank[symbol] * face_value)/100
            amounts += '$' + format(amount,'0.2f') + '\t'
            total += amount
            print(f"{symbol}\t{face_value}\t{count}\t{amount}\t{total:0.2f}")
        assert(total == self.total())
        return header + '\n'\
                + counts + '\n'\
                + amounts + '\t$' + str(total) + '\n'

    def __repr__(self):
        return self.bank.__repr__()

    def __sub__(self, less):
        print(less)
        return Cash(self.total() - less.total())

    def total(self):
        ''' Total value of tbe bag '''
        total = 0
        for symbol, face_value in DENOMINATIONS:
            total += self.bank[symbol] * face_value
        return float(total)/100

    def noop(self):
        ''' just to avoid too-few-public-methods '''

print(Cash(495))
#print(Cash(5896))
#print(Cash(896))
#print(f"{Cash(896)!r}")

#purchase = Cash(495)
#cash_tendered = Cash(2000)
#print(purchase, cash_tendered)
#change = cash_tendered - purchase
#print(f"{change}")
#def cash_back(cash_tendered=0, purchase_price=0):
#    pass
#class CashDrawer():
#    '''
#    Payments go into the cash drawer and change comes from it.
#    '''
#
#    __init__(self, twenties = 5, tens = 5, twos = 0, ones = 20,\
#            fifty_cent_pieces = 0, quarters = 40, dimes = 50,\
#            nickels = 40, pennies = 100):
#        self.bank = {TWENT" : twenties
#        self.tens = tens
#        self.ones = ones
#        self.fifty_cent_piece = fifty_cent_pieces
#        self.quarters =
#
