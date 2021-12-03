def solution(lines):
    increases = [x > lines[i] for i, x in enumerate(lines[1:])]
    return len([inc for inc in increases if inc])


if __name__ == '__main__':
    with open('input') as f:
        puzzle = [int(x) for x in f]

    print(solution(puzzle))
