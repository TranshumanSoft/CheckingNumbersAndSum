import re
myfile = open('regex_sum_288690.txt')
numlist = list()
for line in myfile:
    line = line.rstrip()
    num = re.findall('[0-9]+', line)
    if len(num) == 0:
        continue
    for i in num:
        numlist.append(i)
total = 0
for i in numlist:
    i = int(i)
    total = total + i
print(total)