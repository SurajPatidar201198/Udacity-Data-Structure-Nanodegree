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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
final_list=[]
for item in texts:
    for i in range(2):
        if item[i] not in final_list:
            final_list.append(item)
for item in calls:
    for i in range(2):
        if item[i] not in final_list:
            final_list.append(item[i])

print(f"There are {len(final_list)} different telephone numbers in the records.")
