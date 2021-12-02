puzzle_in = [int(val) for val in open("input", "r").readlines()]

count = sum([1 if pair[0] < pair[1] else 0 for pair in zip(puzzle_in[:-1], puzzle_in[1:])])

print(count)
