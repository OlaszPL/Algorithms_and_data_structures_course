# Wymiana walut
# K[x][y] - kurs wymiany x na y

# Chcemy znaleźć taki cykl aby zarobić

# Algorytm Bellmana-Forda (ze sprawdzaniem czy nie mamy ujemnych cykli)
# ważnym krokiem jest weryfikacja - czy nie zacznie kręcić się w kółko na ujmenym cyklu

# Możemy przejść na ln(a * b) = lna + lnb (przerabiamy macierz na macierz logarytmów)

# Szukamy ujemnego cyklu (na logarytmach - de facto dla ułamków), bo dzielenie przez ułamki zwiększa ilość
# Jak się nie wykonał w pętli ani razu relax, to można przerwać pętlę.

# Bellman-Ford nie wymaga aby cykl wrócił do startu

# Jakby był niespójny to dodajemy sztuczny wierzchołek i łączymy go z każdym wierzchołkiem
# w tym grafie (o neutralnej wadze np 1). I dzięki temu nie uruchamiamy za wiele razy algorytmu.