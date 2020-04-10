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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
print('First record of texts, {incoming} texts {answering} at time {time}'.format(incoming=texts[0][0], answering=texts[0][1], time=texts[0][2]))
print('Last record of calls, {incoming} calls {answering} at time {time}, lasting {during} seconds'.format(incoming=calls[-1][0], answering=calls[-1][1], time=calls[-1][2], during=calls[-1][3]))