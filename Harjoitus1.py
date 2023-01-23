# Parit pikanäppäimet:
#V SCoden komentopaletti         Ctrl+Shift+P
# Rivien kommentointi            Ctrl + ' (Windows)

# Koodi, joka kysyy viisi nimeä ja tulostaa ne listaan nimeltä "nimet"

nimet = []


#for i in [1, 6]:
    #nimi = input('Anna nimi: ' + str(i) + ': ')
    #nimet.append(nimi)

while len(nimet) < 5:
    nimi = input('Anna nimi: ')
    nimet.append(nimi)        

print(nimet)
