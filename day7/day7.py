def load_data():
  return open(f"input.txt", 'r').read().splitlines()

data = load_data()
tach = {data[0].index('S')}
A = 0
for line in data:
    for c in range(len(line)):
        if line[c] == '^' and c in tach:
            tach.remove(c)
            tach.add(c - 1)
            tach.add(c + 1)
            A += 1
print(A)