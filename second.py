def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    cislo = int(cislo)

    jednotky_a_nact = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět", "deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct",]
    desitky = ["dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    if cislo < 20:
        return jednotky_a_nact[cislo]
    elif cislo < 100:
        if cislo % 10 == 0:
            return desitky[(cislo - 20) // 10]
        else:
            return desitky[(cislo // 10) - 2] + " " + jednotky_a_nact[cislo % 10]
    if cislo == 100:
        return "sto"
    
if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)