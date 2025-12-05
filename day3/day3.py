def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.readlines()
    
def max_joltage_v1(bank):
    print(len(bank)-2)
    print(bank[0:len(bank)-1])
    digit1 = max(bank[0:len(bank)-2])
    idx = bank.index(digit1)
    digit2 = max(bank[idx+1:])
    print(f"Max Joltage of {bank} = {digit1}{digit2}")
    return int(digit1 + digit2)

def max_joltage_v2(bank,switches_left):
    if switches_left == 0: return ""
    if len(bank) == switches_left: return bank
    
    # figure out candidate digits
    cand = bank[0:len(bank)-(switches_left-1)]
    print(f"Cand: {cand}, Switches: {switches_left}")
    # new digit is the max of the candidates
    new_digit = max(cand) if len(bank) > switches_left else cand[0]
    idx = bank.index(new_digit)

    return new_digit + max_joltage_v2(bank[idx+1:],switches_left-1)

s = 0

banks = load_data("input.txt")
for bank in banks:
    print(f"Bank: {bank.strip()}")
    n = int(max_joltage_v2(bank.strip(),12))
    print(f"Final: {n}")
    s += n
print(s)