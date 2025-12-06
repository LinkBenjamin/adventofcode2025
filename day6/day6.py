from functools import reduce
from operator import mul, add

def load_data(filename):
    x = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            x.append(line.strip().split())
    
    return x

def work_problem(data, i):
    rows = len(data)-1
    symbol = data[rows][i]
    total = 0
    match symbol:
        case "+":
            for row in data:
                if row[i] != '+':
                    total += int(row[i])
        case '-':
            for row in data:
                if row[i] != '-':
                    total -= int(row[i])
        case '*':
            for c, row in enumerate(data):
                if c == 0:
                    total = int(row[i])
                else:
                    if row[i] != '*':
                        total *= int(row[i])
        case '/':
            for row in data:
                if row[i] != '/':
                    total /= int(row[i])
    return total
    
def work_problem_2(data, i):
    return 0

d = load_data("input.txt")
s = 0
for x in range(0,len(d[0])):
    s += work_problem(d,x)

print(s)
