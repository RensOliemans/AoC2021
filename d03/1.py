def solution(lines):
    transposed = list(map(list, zip(*lines)))
    c = len(transposed[0])
    gamma = int(f'0b{"".join([str(int(sum([int(x.strip()) for x in y]) > c / 2)) for y in transposed])}', 2)
    return gamma * (pow(2, len(transposed)) - 1 - gamma)


if __name__ == '__main__':
    with open('input') as f:
        puzzle = [x.strip() for x in f]

    print(solution(puzzle))
