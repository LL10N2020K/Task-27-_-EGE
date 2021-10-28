with open('27-27b.txt') as f:
    n = int(f.readline())

    k = {0}

    for _ in range(n):
        pair = list(map(int, f.readline().split()))
        combinations = {x + y for x in k for y in pair}
        k = {x%16: x for x in sorted(combinations)}.values()

    print(max(x for x in k if x%16 != 10))


