def load_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
       return f.readlines()

data = load_data("input.txt")

# Part 1 solution

count = 0
d = 50
for turn in data:
    # print(f"Start at {d}")
    # print(f"Turn: {turn.strip()}")
    direction = -1 if turn[0:1] == "L" else 1
    clicks = int(turn[1:]) % 100 # If the turn is 100 clicks we're back where we are right now... so only move the remainder of 100 to eliminate any of the extra cycles

    change = direction * clicks # Left = negative clicks, right = positive clicks
    # print(f"Change: {change}")
    d += (100 + change)
    d %= 100
    if d == 0: count += 1

print(f"Count: {count}")

# Part 2 Solution

count = 0
dial = 50

def move_left():
    if dial == 0:
        return 99
    else:
        return dial - 1
    
def move_right():
    if dial == 99:
        return 0
    else: return dial + 1

for turn in data:
    direction = turn[0:1]
    distance = int(turn[1:])
    print(f"Turn: {turn}")

    for _ in range(0,distance):
        if direction == "L":
            dial = move_left()
        else:
            dial = move_right()
        if dial == 0: count +=1

    print(f"dial: {dial}")
print(f"Count: {count}")