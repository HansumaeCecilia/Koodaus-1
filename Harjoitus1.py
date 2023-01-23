# Parit pikanäppäimet:
#V SCoden komentopaletti         Ctrl+Shift+P
# Rivien kommentointi            Ctrl + ' (Windows)

# Koodi, joka kysyy viisi nimeä ja tulostaa ne listaan nimeltä "nimet"

nimet = []

#Vaihtoehto 1

#nimi = input('Anna nimi: ' + str(i) + ': ')
#nimet.append(nimi)
#nimi = input('Anna nimi: ' + str(i) + ': ')
#nimet.append(nimi)
#nimi = input('Anna nimi: ' + str(i) + ': ')
#nimet.append(nimi)
#nimi = input('Anna nimi: ' + str(i) + ': ')
#nimet.append(nimi)
#nimi = input('Anna nimi: ' + str(i) + ': ')
#nimet.append(nimi)

# Vaihtoehto 2

#for i in [1, 6]:
    #nimi = input('Anna nimi: ' + str(i) + ': ')
    #nimet.append(nimi)

# Vaihtoehto 3

#while True:
    #nimi = input('Anna nimi: ')
    #nimet.append(nimi)   
    #if len(nimet) < 5:
        #break

# Vaihtoehto 4

while len(nimet) < 5:
    nimi = input('Anna nimi: ')
    nimet.append(nimi)        

print('Nimet: ', nimet)
