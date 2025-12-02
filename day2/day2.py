def load_data(filename):
    with open(filename, "r", encoding='utf-8') as f:
        return f.read().split(",")

def parse_entry(entry):
    d = entry.split('-')
    return (int(d[0]),int(d[1]))

def is_invalid_v1(value):
    #Since we're only looking to see if half the string is equal to the other half, odd lengths are false.
    if len(value) % 2 == 1: return False

    # Calculate the midpoint
    a = len(value)
    mp = int((a/2))

    # if one side is the same as the other, it's true.  Otherwise, it's false.
    if value[0:mp] == value[mp:]: 
        return True
    else:
        return False
    
def get_divisors(number):
    r = []
    max = int(number/2) + 1
    for x in range(1,max):
        if number % x == 0: r.append(x)
    return r

def is_invalid_v2(value):
    # New rules mean we can have odd counts because we can repeat more than 2 times.
    l = len(value)

    # Solution: look at divisors of the length - those are the patterns we have to check
    div = get_divisors(l)

    for d in div:
        # divide the string into equally-sized parts
        parts = [value[i:i+d] for i in range(0, l, d)]
        c = parts.count(parts[0])
        if c == len(parts): return True

    return False

invalid = []
data = load_data("input.txt")
for e in data:
    r = parse_entry(e)
    for x in range(r[0], r[1]+1):
        if is_invalid_v2(str(x)): 
            print(f"Appended {x}")
            invalid.append(x)
print(len(invalid))
print(sum(invalid))