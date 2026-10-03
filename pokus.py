def faktorial(x):

    if x == 1:
        return 1
    vysledek = x * faktorial(x - 1)

    return vysledek

if __name__ == "__main__":
    vysledek = faktorial(2)
    print(vysledek)