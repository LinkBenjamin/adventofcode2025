from functools import lru_cache

def load_data(filename):
    d = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            key, value = line.split(":", 1)
            d[key.strip()] = value.strip().split()
    return d

def count_paths_1(k, d):
    count = 0
    for o in d[k]:
        if "out" in o: 
            count += 1
        else:
            count += count_paths_1(o,d)
    return count


def count_paths_2(k, d):

    @lru_cache(None)
    def helper(node, has_dac, has_fft):
        total = 0
        for o in d[node]:
            new_has_dac = has_dac or (o == "dac")
            new_has_fft = has_fft or (o == "fft")

            if "out" in o:
                if new_has_dac and new_has_fft:
                    total += 1
            else:
                total += helper(o, new_has_dac, new_has_fft)

        return total

    return helper(k, False, False)

data = load_data('small.txt')

paths1 = count_paths_1("you", data)
print(paths1)

data2 = load_data('input.txt')

paths2 = count_paths_2("svr", data2)
print(paths2)