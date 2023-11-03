#!/usr/bin/python3

mbox = dict()
try:
    f = open("mbox-short.txt")
    for row in f:
        row = row.strip()
        if row.startswith("From: "):
            strarr = row.split()
            sender_id = strarr[1]
            if sender_id not in mbox:
                mbox[sender_id] = 1
            else:
                mbox[sender_id] += 1
finally:
    f.close()

print(mbox)
