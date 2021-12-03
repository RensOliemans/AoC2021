def solution(lines):
    return oxy_co2(lines, 0, False) * oxy_co2(lines, 0, True)


def oxy_co2(lines, pos, invert):
    if len(lines) == 1:
        return int(lines[0], 2)

    most_common = int(len([n[pos] for n in lines if n[pos] == '1']) / len(lines) >= 0.5)
    if invert:
        most_common = 1 - most_common
    lines = [p for p in lines if p[pos] == str(most_common)]
    return oxy_co2(lines, pos + 1, invert)


if __name__ == '__main__':
    with open('input') as f:
        puzzle = [x.strip() for x in f]

    print(solution(puzzle))
