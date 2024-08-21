# Autostrady
# mamy płaszczyznę i punkty na płaszczyźnie, te punkty reporezuntują miasta (x1, y1), ... (xi, yi)

# Możemy poprowadzić autostradę między każdą parą miast (autostrada zawsze po linii prostej)
# --> autostrada jest w metryce euklidesowej

# Autostrada buduje się w różnym czasie - w zależności od tego jak jest długa.
# d = sqrt((xi - xj)^2 + (yi - yj)^2)
# c_ij = ceil(d) --> czas potrzebny do budowy autostrady

# Chcemy wybudować autostrady dwukierunkowe, tak aby się dało przejechać między dwoma miastami
# (niekoniecznie bezpośrednio)

# chcemy aby min_czas i max_czas budowy były jak najbliżej sobie
# (czas_max - czas_min) --> to chcemy minimalizować

# minimalne drzewo rozpinające w grafie pełnym (w większości przypadków)

# Kolejne drzewa rozpinające z kolejnych krawędzi -- i też nie, nie miałem siły słuchać.

# Po posortowaniu E, dla każdej krawędzi szukamy drzewa rozpinającego 
# Złożoność O(V^4log*V)

# Zrobione jako offline