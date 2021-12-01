from _01 import puzzle, measure


def solution(lines):
    increases = [x > lines[i] for i, x in enumerate(lines[1:])]
    return len([inc for inc in increases if inc])


if __name__ == '__main__':
    print(solution(puzzle))
    measure(lambda: solution(puzzle))
