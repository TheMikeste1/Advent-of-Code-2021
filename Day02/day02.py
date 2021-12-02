# %% Part 1
puzzle_in = open("input").readlines()

commands = list(map(lambda t: (t[0], int(t[1])), 
                    map(lambda s: s.split(), puzzle_in)))

depth_movement = 0
horizontal_movement = 0
for cmd, amount in commands:
    match cmd:
        case "forward":
            horizontal_movement += amount
        case "up":
            depth_movement -= amount
        case "down":
            depth_movement += amount
        
print(f"Part 1: {depth_movement * horizontal_movement}")

# %% Part 2
depth_movement = 0
horizontal_movement = 0
aim = 0
for cmd, amount in map(lambda t: (t[0], int(t[1])), 
                    map(lambda s: s.split(), puzzle_in)):
    match cmd:
        case "forward":
            horizontal_movement += amount
            depth_movement += aim * amount
        case "up":
            aim -= amount
        case "down":
            aim += amount
        
print(f"Part 2: {depth_movement * horizontal_movement}")