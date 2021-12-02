from functools import reduce

from _02 import puzzle, measure, test


def solution(lines):
    lines = [(x[0], (-1 if x[0] == 'u' else 1) * int(x[-2])) for x in lines]

    def add(current, new):
        aim, hpos, depth = current
        command, x = new
        if command == 'f':
            return aim, hpos + x, depth + x * aim
        return aim + x, hpos, depth

    aim, hpos, depth = reduce(lambda a, b: add(a, b), lines, (0, 0, 0))
    return hpos * depth


if __name__ == '__main__':
    print(solution(puzzle))
    measure(lambda: solution(puzzle))
