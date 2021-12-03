def solution(lines):
    increases = [lines[i+3] > lines[i] for i, x in enumerate(lines[1:-2])]
    return len([inc for inc in increases if inc])


if __name__ == '__main__':
    with open('input') as f:
        puzzle = [int(x) for x in f]

    print(solution(puzzle))
