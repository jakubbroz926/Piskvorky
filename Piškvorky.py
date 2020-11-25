def rozdělení():
    print("=" * 40)


def osloveni():
    print("=" * 27)
    print("Vítej ve hře PIŠKVORKY !!")


def pravidla(velikost_pole):
    print("Pravidla hry: ")
    print("Každý hráč může umístit jednu značku nebo kámen za tah na pole o velikosti {}x{}.\n"
          "Vítězem je ten hráč, který umístí tři své značky buď v\n"
          "* horizontální,\n"
          "* vertikální nebo \n"
          "* šikmé rovině\n"
          "Pojďme hrát".format(velikost_pole, velikost_pole))
    return velikost_pole


def generování_pole(velikost_pole):
    pole = []
    for i in range(1,velikost_pole+1):
        linka = []
        viditelna_linka = []
        print("-" * 6)
        for j in range(1,velikost_pole+1):
            viditelna_linka.append(str(" "))
            linka.append(str((j + velikost_pole * i )-velikost_pole))
            číslice = str((j + velikost_pole * i )-velikost_pole)
            radek = "|".join(viditelna_linka)
        print(radek)
        pole.append(linka)
    return pole


def hrac(symbol):
    rozdělení()
    pozice_pro_znak = int(input(f"Player {symbol} | Please enter your move number: "))
    rozdělení()
    rozdělení()
    return pozice_pro_znak

def vyobrazení_aktuálního_pole(aktuální):
    for i in range(len(aktuální)):
        radek = []
        for j in range(len(aktuální[i])):
            if aktuální[i][j].isdigit():
                radek.append(" ")
                radky = "|".join(radek)
            else:
                radek.append(aktuální[i][j])
                radky = "|".join(radek)
        print("-" * 6)
        print(radky)





def zmena_pole(pozice_pro_znak,symbol,zapisovací_pole):
    for i in range(len(zapisovací_pole)):
        for j in range(len(zapisovací_pole[i])):
            if str(pozice_pro_znak) == zapisovací_pole[i][j]:
                zapisovací_pole[i][j] = symbol



    return zapisovací_pole


def hlavni():
    osloveni()
    velikost_pole = pravidla(3)
    původní_pole = generování_pole(velikost_pole)
    smyčka(velikost_pole,původní_pole)

def smyčka(velikost_pole,pole):
    symbols = ["o", "x"]
    i = velikost_pole ** 2
    while i != 0:
        symbol = (symbols[1] if i % 2 == 0 else symbols[0])
        výsledek = zmena_pole((hrac(symbol)),symbol,pole)
        vyobrazení_aktuálního_pole(výsledek)

        i -= 1

if __name__ == '__main__':
    hlavni()
