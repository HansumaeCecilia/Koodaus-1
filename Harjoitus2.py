# Funktioita

#print(x) # Tulostetaan
#x = input() # Luetaan merkkijono muuttujaan x
#str(x) # Muutetaan x merkkijonoksi
#.append(x)

# Vaihtoehto 1

def kysy_nimi():
    nimi = input('Anna nimesi ')
    return nimi

# Vaihtoehto 2

def kysy_nimet(lkm):
    nimet = []
    while len(nimet) < lkm:
        nimi = kysy_nimi()
        nimet.append(nimi)
    return nimet

# Vaihtoehto 3

# def kysy_nimet_rekusriolla(jäljellä, nimet = None):
#     if jäljellä == 0:
#         return nimet
#     if nimet is None:
#         nimet = []
#     nimi = kysy_nimi()
#     return kysy_nimet_rekusriolla(jäljellä - 1, nimet + [nimi])

if __name__ == "_main_":
    print('Testataan kolmella nimellä')
    nimilista = kysy_nimet(3)
    print(nimilista)