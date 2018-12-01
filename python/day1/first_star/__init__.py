def input_data():
    with open("/Users/mikes/Projects/AoC2018/python/day1/input1.txt") as f:
        for line in f:
            yield int(line.strip())


def solve_day1(base=0):
    total = base + sum(input_data())
    print(f"Result when base is 0 will be {total}")


if __name__ == '__main__':
    solve_day1()
