from pprint import pformat, pprint
from time import ctime
import time

aikaleima = time.time()

esimerkki_kuvio = {
    "nimi": "Esimerkki",
    "tyyppi": "monikulmio",
    "luotu": ctime(aikaleima),
    "pisteet": [
        {"x": 10, "y": 20, "z": 30},
        {"x": 20, "y": 5, "z": 10},
        {"x": 30, "y": 15, "z": 20},
    ]
}

pprint(esimerkki_kuvio, sort_dicts=False)

esimerkki_kuvio_muotoiltu_teksti = pformat(esimerkki_kuvio)

# Muutetaan muotoiltu teksti isoiksi kirjaimiksi ja tulostetaan
# Huom: \n  =  rivinvaihto
print("Muotoiltu teksti:\n", esimerkki_kuvio_muotoiltu_teksti.upper())