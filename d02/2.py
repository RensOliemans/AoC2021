from functools import reduce


def solution(lines):
    lines = [(x[0], (-1 if x[0] == 'u' else 1) * int(x[-2])) for x in lines]

    def add(current, new):
        aim, h_pos, depth = current
        command, x = new
        return (aim, h_pos + x, depth + x * aim) if command == 'f' else (aim + x, h_pos, depth)

    _, h, d = reduce(add, lines, (0, 0, 0))
    return h * d


if __name__ == '__main__':
    with open('input') as f:
        puzzle = f.readlines()

    print(solution(puzzle))
