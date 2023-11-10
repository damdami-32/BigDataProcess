import calendar
import sys

day_lst = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
sort_lst = []

with open(sys.argv[1], "r") as input_file:
    for line in input_file:
        line = line.strip()

        colon = line.split(",")
        days = colon[1].split("/")
        days = list(map(int, days))
        day = calendar.weekday(int(days[2]), int(days[0]), int(days[1]))

        lst = [colon[0], day_lst[day], colon[2], colon[3]]

        sort_lst.append(lst)

sort_lst.sort(key=lambda x: (x[0], x[1][2], x[1][0], x[1][1]))

result_lst = []
pivot_lst = []

for item in sort_lst:
    flag = 1
    pivot = [item[0], item[1]]
    
    for p in pivot_lst:
        if pivot == p:
            flag = 0

    if flag:
        car = 0
        num = 0
        for rec in sort_lst:
            rec_lst = [rec[0], rec[1]]
            if pivot == rec_lst:
                car += int(rec[2])
                num += int(rec[3])

        lst = [pivot[0], pivot[1], car, num]
        result_lst.append(lst)

        pivot_lst.append(pivot)

with open(sys.argv[2], "w") as output_file:
    for item in result_lst:
        output_file.write(f"{item[0]},{item[1]} {item[2]},{item[3]}\n")