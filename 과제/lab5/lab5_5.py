import json

with open('lab5\movies.json', encoding="utf-8") as datafile:
    jsondata = json.load(datafile)

movies = list(jsondata["boxOfficeResult"]['dailyBoxOfficeList'])

sum = 0
for movie in movies:        #movies는 dictionary다.
    sum += int(movie['salesAmt'])

print(sum)