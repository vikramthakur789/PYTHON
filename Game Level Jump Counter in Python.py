def game_jumps(total_levels=10):
    total_jumps = 0
    for level in range(1, total_levels + 1):
        side_a_jumps = level
        side_b_jumps = level
        print(f"Level {level}: Side A jumps = {side_a_jumps}, Side B jumps = {side_b_jumps}")
        total_jumps += side_a_jumps + side_b_jumps
    print(f"\nTotal jumps to reach level {total_levels}: {total_jumps}")

# Run the function
game_jumps()
