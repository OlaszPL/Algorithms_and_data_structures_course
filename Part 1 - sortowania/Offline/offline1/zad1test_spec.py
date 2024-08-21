# zad1test_spec.py

ALLOWED_TIME = 3


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
# k, len(list), maxint
  (1, 20, 100),
  (30, 30, 100),
  (10, 100, 1000),
  (25, 100, 1000),
  (25, 2000, 10000),
  (1, 10000, 2**24),
  (10, 10000, 2**24),
  (1, 100000, 2**24),
  (5, 100000, 2**24),
  (1, 1000000, 2**24),
]

