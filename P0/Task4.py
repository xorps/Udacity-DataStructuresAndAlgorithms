"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def make_whitelist():
    """ if the number is in here, it's not a telemarketer """
    res = set()
    # add outgoing sms and receiving sms numbers
    for text in texts:
        res.add(text[0])
        res.add(text[1])
    # add receiving calls
    for call in calls:
        res.add(call[1])
    return res

whitelist = make_whitelist()
outgoing_calls = (call[0] for call in calls)
suspects = sorted(set(s for s in outgoing_calls if s not in whitelist))

print('These numbers could be telemarketers:')
for s in suspects:
    print(s)
