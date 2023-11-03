str = "X-DSPAM-Confidence:0.8475"

only_str = str[:str.find(':')+1]
num = float(str[str.find(':') + 1: ])
print(num)