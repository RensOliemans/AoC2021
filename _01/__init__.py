from timeit import timeit

with open('input') as f:
    puzzle = [int(x) for x in f]


def measure(func):
    n = 10000
    print(f'{timeit(func, number=n)/n:.2E}s')
