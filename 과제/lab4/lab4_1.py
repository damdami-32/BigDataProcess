try:
    name = input()
    f = open(name, "rt")
    text = f.read()
    print(text.upper())
except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    f.close