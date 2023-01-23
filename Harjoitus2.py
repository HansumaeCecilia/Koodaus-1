# Funktioita

#print(x) # Tulostetaan
#x = input() # Luetaan merkkijono muuttujaan x
#str(x) # Muutetaan x merkkijonoksi
#.append(x)

def kysy_nimi():
    nimi = input('Anna nimesi ')
    return nimi

def kysy_nimet(lkm):
    nimet = []
    while len(nimet) < lkm:
        nimi = kysy_nimi()
        nimet.append(nimi)
    return nimet

nimilista = kysy_nimet(3)
print(nimilista)