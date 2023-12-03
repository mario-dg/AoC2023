file = "puzzle_records.txt"

num_red_cubes = 12
num_green_cubes = 13
num_blue_cubes = 14

with open(file) as f:
    sets_pow = []
    for line in f:
        game_sets_split = line.split(": ")
        game_id = int(game_sets_split[0].replace("Game ", ""))

        max_red = -1
        max_green = -1
        max_blue = -1
        for set in game_sets_split[1].split("; "):
            for color in set.split(", "):
                if "red" in color:
                    max_red = max(max_red, int(color.replace("red", "")))
                elif "green" in color:
                    max_green = max(max_green, int(color.replace("green", "")))
                elif "blue" in color:
                    max_blue = max(max_blue, int(color.replace("blue", "")))
        print(max_red, max_green, max_blue)
        sets_pow.append(max_red * max_green * max_blue)

print(sum(sets_pow))

