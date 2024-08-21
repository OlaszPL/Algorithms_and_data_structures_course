# 1. zmienne
# 2. formuła w formacie ZCNF

# (x v y) ^ (~x v z) ^ (~z v ~y)

# Zapisujemy to jako implikacje (wtedy widać graf)

# Robi się to przez silnie spójne składowe --> mamy graf acykliczny.

# Jak mamy wartościowanie to szukamy tak by nie było połączenia z fałszu wynika prawda (bo to nie prawda).
# Do tego co wyszło na końcu możemy sobie wpisać 1 (bo to jest zawsze dobrze) i cofamy się do poprzednich spójnych
# i sprawdzamy, czy możemy wpisać w nie 1 (jak na samej górze dojdziemy do 0 to sprzeczność)
# => formuła nie jest prawdziwa.

