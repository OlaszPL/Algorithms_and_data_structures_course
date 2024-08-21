# # Zadanie ze spływaniem wody.
# # Pojemniki są opisywane jako [(x1, y1, x2, y2), ...] - dół, góra dla jednego pojemnika
# # Odkręcamy kran i wlewamy L litrów wody. Ile pojemików zostane całkowicie zapełnionych.
# # Trzeba uwzględniać to, że niektóre mogą być częściowo napełnione.
# # Zawsze najpierw napełni się ten na samym dole.

# # Można to zrobić bez sortowania.
# # Trzeba przekształcić L w H (wysokość słupa wody)

# # Określimy wysokość i dla określonej wysokości określimy ile trzeba wody wlać --> to jest łatwiejsze.
# # Metodą bisekcji, w kilku iteracjach (jakby połówkowe wyszukiwanie).

# Mamy serię pojemników z wodą, połączonych (każdy z każdym) rurami. Pojemniki maja kształty prosto-
# kątów (2d), rury nie maja objętości (powierzchni). Każdy pojemnik opisany jest przez współrzędne lewego
# górnego rogu i prawego dolnego rogu. Wiemy, ze do pojemników nalano A wody (oczywiście woda rurami
# spłynęła do najniższych pojemników). Obliczyć ile pojemników zostało w pełni zalanych.


from random import randint

def generate_container():
    x1 = randint(0, 14)
    y1 = randint(0, 14)
    x2 = randint(x1 + 1, 15)  
    y2 = randint(y1 + 1, 15)
    return (x1, y1, x2, y2)

def zad4_zamiatanie(T, L):
    gory = []
    doly = []
    V = 0

    pojemnik = T[0]
    x1, y1, x2, y2 = pojemnik

    gory.append((y2, x2-x1))
    doly.append((y1, x2-x1))

    for pojemnik in T[1:]:
        x1, y1, x2, y2 = pojemnik
        dol = (y1, x2-x1)
        gora = (y2, x2-x1)

        for i in range(len(gory)+1):
            if i == len(gory):
                gory.append(gora)
                break
            if gory[i][0] > gora[0]:
                gory.insert(i, gora)
                break

        for i in range(len(doly)+1):
            if i == len(doly):
                doly.append(dol)
                break
            if doly[i][0] > dol[0]:
                doly.insert(i, dol)
                break

    if len(gory) == 0 or len(doly) == 0:
        return
    
    #print(gory)
    #print(doly)

    poprzednia_wysokosc = 0
    szerokosc = 0
    ile_zapelnionych = 0

    for i in range(len(gory) + len(doly)):

        czy_dodac = False
        #print(V)
        
        if(len(doly) == 0):
            V += szerokosc*(gory[0][0]-poprzednia_wysokosc)
            szerokosc -= gory[0][1]
            poprzednia_wysokosc = gory[0][0]
            gory.pop(0)
            czy_dodac = True

        elif(doly[0][0] < gory[0][0]):
            V += szerokosc*(doly[0][0]-poprzednia_wysokosc)
            szerokosc += doly[0][1]
            poprzednia_wysokosc = doly[0][0]
            doly.pop(0)
        else:
            V += szerokosc*(gory[0][0]-poprzednia_wysokosc)
            szerokosc -= gory[0][1]
            poprzednia_wysokosc = gory[0][0]
            gory.pop(0)
            czy_dodac = True

        if(V > L):
            break

        if(czy_dodac):
            ile_zapelnionych += 1

    return ile_zapelnionych


def zad4_wysokosc_slupa(T, L):
    H = 1
    slup = []

    maksH = 0
    for i in range(len(T)):
        maksH = max(T[i][3], maksH)

    while H <= maksH:

        V_of_current_layer = 0
        for cnt in T:
            if cnt[1] < H and cnt[3] >= H:
                V_of_current_layer += cnt[2]-cnt[0]

        if(len(slup) > 0):
            slup.append(V_of_current_layer+slup[-1])
        else:
            slup.append(V_of_current_layer)

        H += 1

    print(slup)

    left = 0
    right = len(slup)
    middle = int((right+left)/2)

    while middle != len(slup)-1 and not (slup[middle] <= L and slup[middle+1] > L):

        if(slup[middle] > L):
            right = int((right+left)/2)
        else:
            left = int((right+left)/2)

        middle = int((right+left)/2)

    #print(middle)

    ile_zapelnionych = 0
    for cnt in T:
        if cnt[3] <= middle+1:
            ile_zapelnionych += 1
    
    return ile_zapelnionych




#containers = [(8, 2, 14, 3), (0, 2, 6, 12), (14, 3, 15, 12), (14, 2, 15, 9), (1, 6, 11, 7)]
containers = []

for i in range(100):
    containers.append(generate_container())

print(containers)

print("Ile zapełnionych pojemników: ", zad4_wysokosc_slupa(containers, 1000))
print("Ile zapełnionych pojemników: ", zad4_zamiatanie(containers, 1000))