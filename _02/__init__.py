from timeit import timeit

with open('2') as f:
    puzzle = f.readlines()


def measure(func, n=10000):
    print(f'{timeit(func, number=n)/n:.2E}s')
