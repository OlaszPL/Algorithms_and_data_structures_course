import random
from collections import defaultdict


def random_matrix(n, range_=(0, 100)):
    return [[random.randint(*range_) for _ in range(n)] for _ in range(n)]


def random_tests(fn, size=(1, 30), range_=(0, 100), samples=25):
    passed = 0
    for i in range(1, samples + 1):
        n = random.randint(*size)
        matrix = random_matrix(n, range_)
        init_counts = defaultdict(int)
        for row in matrix:
            for val in row:
                init_counts[val] += 1
        print(f'===== Test #{i}: =====')
        print(f'Input array ({n} x {n}):')
        print(*matrix, sep='\n', end='\n\n')
        fn(matrix)
        final_counts = defaultdict(int)
        for row in matrix:
            for val in row:
                final_counts[val] += 1
        no_dropped_values = init_counts == final_counts
        is_correct = no_dropped_values
        passed += is_correct
        print('Result array:')
        print(*matrix, sep='\n', end='\n\n')
        print('Is correct?:', is_correct)
        if not is_correct:
            print('Dropped values?:', not no_dropped_values)
        print(f'Tests already passed: {passed}/{i}', end='\n\n\n')
    print('\n===== Final results: =====')
    print(f'Total tests passed: {passed}/{samples}')