num_steps = 6

for r in range(num_steps):
    for c in range(r):
        if c == 0:
            print("#", end='')
        else:
            print(' ', end='')
    print("#")
