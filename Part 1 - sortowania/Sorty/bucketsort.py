# Pseudokodem bo implementacja zależy od struktury danych (i tego jak wydajna jest konkatenacja w każdej z nich)

# Kiedy rozkład jest równomierny lub prawie równomierny.

# BUCKET-SORT(A, n)
#     let B[0 : n – 1] be a new array
#     for i = 0 to n – 1

#     make B[i] an empty list
#     for i = 1 to n

#     insert A[i] into list B[⌊n · A[i]⌋]
#     for i = 0 to n – 1

#     sort list B[i] with insertion sort
#     concatenate the lists B[0], B[1], … , B[n – 1] together in order
#     return the concatenated lists