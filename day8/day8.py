class Box:
    def __init__(self, id, coords):
        self.id = id
        self.x = int(coords[0])
        self.y = int(coords[1])
        self.z = int(coords[2])
    def __str__(self):
        return f"(Box id {self.id}, {self.x}, {self.y}, {self.z})"
    
    def __eq__(self, other):
        if not isinstance(other, Box):
            return NotImplemented  
        return self.x == other.x and self.y == other.y and self.z == other.z
    def __hash__(self):
        return hash((self.x, self.y, self.z))

def load_data(filename):
    return open(filename, 'r', encoding='utf-8').read().split('\n')

def distance(box1, box2):
    return ((box1.x - box2.x) ** 2 + (box1.y - box2.y) ** 2 + (box1.z - box2.z) ** 2) ** 0.5
data = load_data("input.txt")
boxes = []
count = 1
for b in data:
    n = b.split(',')
    boxes.append(Box(count, n))
    count +=1
distances = set()
for box1 in boxes:
    for box2 in boxes:
        if box1 != box2:
            d_val = distance(box1, box2)
            box_pair = [box1, box2]
            box_pair.sort(key=str)
            final_tuple = (d_val, box_pair[0], box_pair[1])
            distances.add(final_tuple)
sorted_distances_list = sorted(distances, key=lambda d: d[0])
thing = []
for x in range(1000):
    thing.append(sorted_distances_list[x])
circuitbox = []

def add_box_to_circuit(b1, b2):
    processed = False
    for item in circuitbox:
        if b1.id in item or b2.id in item:
            item.append(b1.id)
            item.append(b2.id)
            processed = True
    
    if not processed:
        circuitbox.append([b1.id, b2.id])
for t in thing:
    print(f"{t[0], str(t[1]), str(t[2])}")
    add_box_to_circuit(t[1], t[2])
for c in circuitbox:
    print(set(c))
parent = {}
for current_set in circuitbox:
    for number in current_set:
        if number not in parent:
            parent[number] = number

def find(i):
    if parent[i] == i:
        return i
    
    parent[i] = find(parent[i])
    return parent[i]

def union(i, j):
    root_i = find(i)
    root_j = find(j)  
    if root_i != root_j:  
        parent[root_j] = root_i
for current_set in circuitbox:
    numbers = list(current_set) 
    if not numbers:
        continue 
    anchor = numbers[0] 
    for i in range(1, len(numbers)):
        union(anchor, numbers[i])
collapsed_groups = {}
for number, root in parent.items():
    
    final_root = find(number) 
    
    
    if final_root not in collapsed_groups:
        collapsed_groups[final_root] = set()
        
    collapsed_groups[final_root].add(number)
final_collapsed_sets = list(collapsed_groups.values())
sorted_sets = sorted(
    final_collapsed_sets,
    key=len,      
    reverse=True  
)
print(len(sorted_sets[0]) * len(sorted_sets[1]) * len(sorted_sets[2]))