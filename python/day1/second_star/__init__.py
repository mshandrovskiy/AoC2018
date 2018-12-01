import itertools


def input_data():
    with open("/Users/mikes/Projects/AoC2018/python/day1/input1.txt") as f:
        for line in f:
            yield int(line.strip())


def solve_day1(base=0):
    total = base
    encountered = set()
    for freq in itertools.cycle(input_data()):
        total += freq
        if total in encountered:
            print(f"Result when base is 0 will be {total}")
            return
        else:
            encountered.add(total)


if __name__ == '__main__':
    solve_day1()
