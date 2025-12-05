def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.readlines()

data = load_data("input.txt")

def count_neighbors(r,c,rows,cols):
    if data[r][c] != '@': return -1
    # print(f"{data[r][c]} - {r},{c} - {rows},{cols}")
    neighbors = 0
    ro = rows -1
    co = cols -1
    if r > 0:
    # up left
        if c > 0:
            # print("upleft")
            if data[r-1][c-1] != '.': 
                neighbors +=1
    # up
        # print("up")
        if data[r-1][c] != '.': 
            neighbors +=1
    # up right
        if c < co:
            # print("upright")
            if data[r-1][c+1] != '.': 
                neighbors +=1
    # left
    if c > 0:
        # print("left")
        if data[r][c-1] != '.': 
            neighbors +=1
    # right
    if c < co:
        # print("right")
        if data[r][c+1] != '.': 
            neighbors +=1
    # down left
    if r < ro:
        if c > 0:
            # print("downleft")
            if data[r+1][c-1] != '.': 
                neighbors +=1
    # down
        # print("down")
        if data[r+1][c] != '.': 
            neighbors +=1
    # down right
        if c < co:
            # print("downright")
            if data[r+1][c+1] != '.': 
                neighbors +=1

    if neighbors < 4:
        data[r] = data[r][:c] + 'x' + data[r][c+1:]
    return neighbors

rows = len(data)
cols = len(data[0].strip())
total = 0
accessible = 0

def clear_removed():
    for r in range(0, rows):
        for c in range(0,cols):
            if data[r][c] != '@': data[r] = data[r][:c] + '.' + data[r][c+1:]

iterations = 0
while True:
    accessible = 0
    iterations += 1
    for r in range(0,rows):
        for c in range(0,cols):
            # print(data[r][c])
            n = count_neighbors(r,c,rows,cols) 
            # print(n)
            if n < 4 and n >= 0: accessible += 1
    if accessible == 0: break
    total += accessible
    clear_removed()
    print(f"Iteration {iterations}")
    print(data)

print(f"Total: {total}")