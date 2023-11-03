price = [10000, 8000, 7500, 12000, 25000]

for i in map(lambda x : x * 0.8, price):
    print(i, end=', ')
