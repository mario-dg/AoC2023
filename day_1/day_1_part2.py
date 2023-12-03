file = "calibration_values.txt"

str_to_int = {"one": 1,
              "two": 2,
              "three": 3,
              "four": 4,
              "five": 5,
              "six": 6,
              "seven": 7,
              "eight": 8,
              "nine": 9}

all_codes = []
with open(file, 'r') as f:
    for line in f:
        first_num_occ = (-1, -1)
        idx = 0
        for c in line:
            if c.isnumeric():
                first_num_occ = (idx, int(c))
                break
            idx += 1
        first_num_str_occ = sorted([(line.find(k), v) for k, v in str_to_int.items() if k in line])
        if len(first_num_str_occ) > 0:
            first_num_str_occ = first_num_str_occ[0]
            if first_num_str_occ[0] < first_num_occ[0]:
                first_num_occ = first_num_str_occ

        last_num_occ = (-1, -1)
        idx = len(line) - 1
        for c in reversed(line):
            if c.isnumeric():
                last_num_occ = (idx, int(c))
                break
            idx -= 1
        last_num_str_occ = sorted([(line.rfind(k), v) for k, v in str_to_int.items() if k in line])
        if len(last_num_str_occ) > 0:
            last_num_str_occ = last_num_str_occ[-1]
            if last_num_str_occ[0] > last_num_occ[0]:
                last_num_occ = last_num_str_occ
        all_codes.append(int(f"{first_num_occ[1]}{last_num_occ[1]}"))

print(sum(all_codes))
