try:
    f = open("mbox-short.txt", "rt")
    
    len = int(0)
    sum = int(0)

    while True:
        row = f.readline()
        if not row: break

        if row.startswith("X-DSPAM-Confidence"):
            sum += float(row[row.find(':') + 2: ])
            len += 1

    print(sum / len)
except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    f.close