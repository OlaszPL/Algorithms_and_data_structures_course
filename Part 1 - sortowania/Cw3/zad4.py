# W jaki sposób zadeklarować strukturę danych, która pozwala nam na operacje: insert, remove_min, remove_max (złożoność ma być logarytmiczna)
# insert jest logarytmiczny
# struktura z dwoma kopcami (jeden minimalnmy, drugi maksymalny)
# każdy element w każdym kopcu musi pamiętać gdzie jest jego bliźniak (jest w postaci krotki)
# krotki wartość, pointer

# Proszę zaprojektowac strukturę danych przechowującą liczby i pozwalającą na następujące
# operacje (zakładamy, że wszystkie liczby umieszczane w strukturze są różne):
# Init(n). Tworzy zadaną strukturę danych zdolną pomieścić maksymalnie n liczb.
# Insert(x). Dodaje do struktury liczbę x.
# RemoveMin() Znajduje najmniejszą liczbę w strukturze, usuwa ją i zwraca jej wartość.
# RemoveMax() Znajduje największą liczbę w strukturze, usuwa ją i zwraca jej wartość.

class MinMax:
    def __init__(self, size, )