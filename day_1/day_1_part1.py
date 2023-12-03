file = "calibration_values.txt"

all_codes = []
with open(file, 'r') as f:
    for line in f:
        first_num = None
        last_num = None
        for c in line:
            if c.isnumeric():
                first_num = c
                break
        for c in reversed(line):
            if c.isnumeric():
                last_num = c
                break
        all_codes.append(int(f"{first_num}{last_num}"))
        
print(sum(all_codes))
