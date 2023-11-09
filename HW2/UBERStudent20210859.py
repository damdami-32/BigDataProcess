import datetime
import sys

input_file = open(sys.argv[1], "rt")
output_file = open(sys.argv[2], "wt")

day_lst = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
sort_lst = []

for line in input_file:
    line = line.strip()

    colon = line.split(",")
    days = colon[1].split("/")
    days = list(map(int, days))
    day = datetime.date(int(days[2]), int(days[0]), int(days[1])).weekday()

    lst = [colon[0], day_lst[day], colon[2], colon[3]]

    sort_lst.append(lst)

#sort_lst.sort(key=lambda x: (x[0], x[1][2], x[1][0], x[1][1]))

for item in sort_lst:
    output_file.write(f"{item[0]},{item[1]} {item[2]},{item[3]}\n")

input_file.close()
output_file.close()