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
banglore_call=[]

for call in calls:
  if(call[0][0:5]=="(080)"):
    banglore_call.append(call[1])

# print(banglore_call)

area_code_temp=[]
for i in banglore_call:
  if(i.find(')')!=-1):
    last=i.find(')')+1
    area_code_temp.append(i[0:last])
  else:
    area_code_temp.append(i[0:4])

# print(area_code_temp)
set1=set()
for i in area_code_temp:
  if(')' in i):
    last=i.find(')')
    set1.add(i[1:last])
  else:
    set1.add(i)
  
set1=sorted(set1)
print('The numbers called by people in Bangalore have codes:')
for i in set1:
  print(i)


    
#*******************************************************************
print()
called_from_banglore = [call[1] for call in calls if call[0][:5] == '(080)']
print('{0:.2f}'.format(
    (len([phone for phone in called_from_banglore if '(080)' in phone]) / len(called_from_banglore)) * 100),
    'percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')