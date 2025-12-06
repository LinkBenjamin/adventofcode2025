import itertools

def load_data(filename):
    d = []
    fresh = []
    ingredients = []
    with open(filename, 'r', encoding='utf-8') as f:
        d = f.readlines()

    print("Loading Fresh list...")
    for line in d:
        l = line.strip()
        if '-' in l: 
            fresh.append(l)
        elif l == '':
            print("Loading ingredient list...")
        else:
            ingredients.append(l)
    
    return fresh, ingredients

def get_values(f):
    r = f.split('-')
    return int(r[0]), int(r[1])

def merge_freshes(fr):
    pairs = []
    for f in fr:
        start, end = get_values(f)
        pairs.append([start, end])
    pairs.sort()

    merged = []
    for start, end in pairs:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    
    return merged

def count_freshes(f):
    merged = merge_freshes(f)
    count = 0
    for m in merged:
        count += m[1]-m[0] + 1
    return count

def is_fresh(ing, fresh):
    for f in fresh:
        low, high = get_values(f)
        if ing >= low and ing <= high: return True
    
    return False

f, i = load_data("input.txt")

# print(f"Fresh: {f}")
# print(f"Ingredient list: {i}")

count = 0
for ing in i:
    if is_fresh(int(ing), f): 
        # print(f"{ing} is fresh!")
        count +=1

print(f"Ingredient freshness Count: {count}")

print(f"Freshes: {count_freshes(f)}")