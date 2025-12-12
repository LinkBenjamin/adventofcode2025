def load_data(filename):
    coords = []
    with open(filename, 'r', encoding='utf-8') as f:
        for l in f:
            vars = l.strip().split(',')
            coords.append((int(vars[0]),int(vars[1])))
    return coords

def area(a,b):
    return abs(b[1]-a[1]+1) * abs(b[0]-a[0]+1)

data = load_data('input.txt')

rects = []
for d1 in data:
    for d2 in data:
        if d1[0] != d2[0] or d1[1] != d2[1]:
            rects.append([area(d1,d2),d1,d2])

s = sorted(rects, key=lambda x: x[0],reverse=True)

print(s[0])