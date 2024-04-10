import math

def max_srednica(boki,dlugosc_boku):
    # Obliczanie kąta centralnego
    kat_centralny = 360 / boki

    # Obliczanie kąta wpisanego w podstawkę
    kat_wpisany = 180 - kat_centralny

    # Obliczanie promienia okręgu wpisanego
    promien_wpisany = math.sin(math.radians(kat_wpisany / 2))

    # Obliczanie średnicy największego okrągłego obiektu (o średnicy) jaki zmieści się w danym pudle
    srednica_okregu = 2 * promien_wpisany

    return srednica_okregu * dlugosc_boku



print("Największy okrągły obiekt (o średnicy) jaki zmieści się w danym pudle to:", max_srednica(5,10))