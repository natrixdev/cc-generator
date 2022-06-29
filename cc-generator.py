import ccard;import time;x = input('Please choose between:\n\n[1] americanexpress\n[2] mastercard\n[3] discover\n[4] visa\n\n> ')
if x == '1':
    y = ccard.americanexpress();print('Your americanexpress card: ' + str(y))
if x == '2':
    y = ccard.mastercard();print('Your mastercard card: ' + str(y))
if x == '3':
    y = ccard.discover();print('Your discover card: ' + str(y))
if x == '4':
    y = ccard.visa();print('Your visa card: ' + str(y))
time.sleep(10)
