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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
from collections import namedtuple

def is_bangalore(number):
    return number[:5] == "(080)"

def area_code(number):
    return number[:number.index(')') + 1]

def mobile_prefix(number):
    return number[:4]

def is_fixed(number):
    return number[0] == "("

def is_mobile(number):
    return number[0] in '789'

def is_telemarketer(number):
    return number[:3] == "140"

def percent(n):
    return int(round(n * 10000)) / 100

def prefix(number):
    if is_mobile(number): return mobile_prefix(number)
    if is_fixed(number): return area_code(number)
    if is_telemarketer(number): return "140"
    return None

class Call(namedtuple('Call', ['caller', 'to', 'time', 'duration'])):
    def from_bangalore(self):
        return is_bangalore(self.caller)
    
    def to_bangalore(self):
        return is_bangalore(self.to)
    
    def to_prefix(self):
        return prefix(self.to)

def test():
    assert area_code("(123) asfs") == "(123)"
    assert area_code("(1) asdf") == "(1)"
    assert area_code("(52342)23432") == "(52342)"
    assert area_code("()") == "()"
    assert is_bangalore("(080)")
    assert mobile_prefix("78395") == "7839"

def part_A():
    c = sorted(set(c.to_prefix() for c in map(Call._make, calls) if c.from_bangalore()))
    print('The numbers called by people in Bangalore have codes:')
    for it in c:
      print(it)

def part_B():
    total = sum(1 for c in map(Call._make, calls) if c.from_bangalore())
    total_to = sum(1 for c in map(Call._make, calls) if c.from_bangalore() and c.to_bangalore())
    percentage = percent(total_to / total)
    print('{percentage} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(percentage=percentage))

part_A()
part_B()