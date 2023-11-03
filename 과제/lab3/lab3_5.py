num = "901231-1914983"
year = num[0:2]
gender = num[7]

print(year + "년생", end=" ")

if gender == '1':
    print("남자")
else:
    print("여자")