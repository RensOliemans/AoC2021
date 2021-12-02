from d01 import puzzle
from measure import measure


def solution(lines):
    increases = [lines[i+3] > lines[i] for i, x in enumerate(lines[1:-2])]
    print(len([inc for inc in increases if inc]))


if __name__ == '__main__':
    solution(puzzle)
    measure(lambda: solution(puzzle))
