from timeit import timeit


def measure(func, n=10000):
    print(f'{timeit(func, number=n)/n:.2E}s')
