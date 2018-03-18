#!python

'''
CHANGE BACK
Author: Dan George

This program runs a check stand. It asks the clerk for a purchase
total and cash tendered. It counts the change bask to the customer
in old-school style.
'''

DENOMINATIONS = {\
    1: 'penny', 5: 'nickel', 10: 'dime', 25: 'quarter', 50: '50c',\
    100: '$1', 200: '$2', 500: '$5', 1000: '$10', 2000: '$20'}

def bucketize(total, buckets):
    '''
    sort total into the buckets defined by buckets parameter
    return the count and subtotal for each bucket
    '''
    counts = {}
    for value in sorted(iter(buckets), reverse=True):
        count = int(total / value)
        subtotal = value * count
        counts[buckets[value]] = (count, subtotal)
        total -= subtotal
        assert total >= 0
    return counts

def count_back(total, change, denominations):
    ''' count back change -- return the remaining total '''
    for value in sorted(iter(denominations), reverse=False):
        name = denominations[value]
        count, subtotal = change[name]
        if subtotal != 0:
            total += subtotal
            print(f"{count} x {name} for ${total/100.0:0.2f}")
    return total

def prompt(prompt_str):
    '''
    simple prompter expects dollars.cents and returns amount in cents
    '''
    done = False
    while not done:
        try:
            return int(100*(round(float(input(prompt_str)), 2)))
        except (TypeError, ValueError):
            print("Oops, please enter dollars.cents")

def run_check_stand():
    ''' simulating a supermarket check stand '''
    while True:
        try:
            purchase_total = prompt("Purchase total: $")
            cash_tendered = 0
            while cash_tendered < purchase_total:
                cash_tendered += prompt("Cash, please: $")
        except (KeyboardInterrupt, EOFError):
            print("\nThis lane CLOSED")
            return
        change = bucketize(cash_tendered - purchase_total,\
                DENOMINATIONS)
        count_back(purchase_total, change, DENOMINATIONS)
        print("Bye, bye\n")

run_check_stand()
