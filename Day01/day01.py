# %% Part 1
puzzle_in = [int(val) for val in open("input", "r").readlines()]
print(f"Part 1: {sum([1 if pair[0] < pair[1] else 0 for pair in zip(puzzle_in[:-1], puzzle_in[1:])])}")

# %% Part 2
sliding_window_sums = list(map(sum, zip(puzzle_in[:-2], puzzle_in[1:-1], puzzle_in[2:])))
print(f"Part 2: {sum([1 if pair[0] < pair[1] else 0 for pair in zip(sliding_window_sums[:-1], sliding_window_sums[1:])])}")
