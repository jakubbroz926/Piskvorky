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


def conditions(pole, znak):
    answers = dia_check(pole, znak), hor_check(pole, znak), ver_check(pole, znak)
    return any(answers)


def hor_check(pole, znak):
    for seznam in range(len(pole)):
        temp_line = []
        for line in range(len(pole[seznam])):
            if pole[seznam][line] == znak:
                temp_line.append(True)
            else:
                temp_line.append(False)
        if all(temp_line):
            return True
    return False


def ver_check(pole, znak):
    for seznam in range(len(pole)):
        temp_column = []
        for column in range(len(pole[seznam])):
            if pole[column][seznam] == znak:
                temp_column.append(True)
            else:
                temp_column.append(False)
        if all(temp_column):
            return True
    return False


def dia_check(pole, znak):
    ověření1 = []
    for i in range(len(pole)):
        if pole[i][i] == znak:
            ověření1.append(True)
        else:
            ověření1.append(False)
    ověření2 = []
    for i in range(len(pole)):
        if pole[-1 - i][-len(pole) + i] == znak:
            ověření2.append(True)
        else:
            ověření2.append(False)
    testy = [all(ověření1), all(ověření2)]
    return any(testy)


def generování_pole(velikost_pole):
    pole = []
    for i in range(1, velikost_pole + 1):
        linka = []
        viditelna_linka = []
        print("-" * 6)
        for j in range(1, velikost_pole + 1):
            viditelna_linka.append(str(" "))
            linka.append(str((j + velikost_pole * i) - velikost_pole))
            #číslice = str((j + velikost_pole * i) - velikost_pole)
            radek = "|".join(viditelna_linka)
        print(radek)
        pole.append(linka)
    print("-" * 6)
    return pole


def hrac(symbol):
    rozdělení()
    pozice_pro_znak = int(input(f"Hráč {symbol} | Prosím vlož pozici pro symbol "))
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
    print("-" * 6)


def zmena_pole(pozice_pro_znak, symbol, zapisovací_pole):
    for i in range(len(zapisovací_pole)):
        for j in range(len(zapisovací_pole[i])):
            if str(pozice_pro_znak) == zapisovací_pole[i][j]:
                zapisovací_pole[i][j] = symbol

    return zapisovací_pole


def hlavni():
    otázka = input("Chcete hrát piškvorky (ANO/NE)?\n")
    while otázka == "ano":
        osloveni()
        velikost_pole = pravidla(3)
        původní_pole = generování_pole(velikost_pole)
        konec, tvrzení = smyčka(velikost_pole, původní_pole)
        vítez(konec, tvrzení)
        otázka = input("Chcete hrát dál ? (ANO/NE)?\n")
        #nahrání skóre

    print("Konec hry")
    #zde bude vyhodnocení


def smyčka(velikost_pole, pole):
    symbols = [input("Zvol si symbol hráči: "), input("Zvol si symbol hráči: ")]
    i = velikost_pole ** 2
    oblast = pole
    symbol = (symbols[1] if i % 2 == 0 else symbols[0])
    while (not conditions(oblast, symbol)) and (i != 0):
        symbol = (symbols[1] if i % 2 == 0 else symbols[0])
        výsledek = zmena_pole((hrac(symbol)), symbol, pole)
        oblast = výsledek
        if conditions(oblast, symbol):
            vyobrazení_aktuálního_pole(výsledek)
            return symbol, True
        else:
            vyobrazení_aktuálního_pole(výsledek)
        i -= 1
    return symbol, False


def vítez(symbol, důvod):
    if důvod:
        print(f"VÍTĚZÍ HRÁČ SE SYMBOLEM {symbol}!!")
    else:
        print("REMÍZA. HRAJTE ZNOVU!!")


if __name__ == '__main__':
    hlavni()
