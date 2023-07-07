"""Zaproponuj program, który pozwoli użytkownikowi na zdefiniowanie grafu, zgodnie z
poniższymi założeniami:
• Program po uruchomieniu pyta użytkownika jaki graf chce zbudować (skierowany,
nieskierowany, ważony, inny możliwy).
• Użytkownik może podać ilość wierzchołków oraz połączeń pomiędzy nimi.
• Z otrzymanych informacji program wyświetla macierz sąsiedztwa oraz listę sąsiedztwa oraz
wyświetla interpretację graficzną grafu.
Program powinien podejmować zrozumiałą komunikację z użytkownikiem, dane wprowadzane i
wyprowadzane powinny być opatrzone zrozumiałym opisem. Program powinien być zapisany czytelnie,
z zachowaniem zasad czystego formatowania kodu, należy stosować znaczące nazwy zmiennych i
funkcji."""





def graf():

    rodzaj_grafu = input("Jaki graf chcesz zbudować? (skierowany/nieskierowany): ")

    ilosc_wierzcholkow = int(input("Podaj ilość wierzchołków: "))

 

    macierz_sasiedztwa = [[0] * ilosc_wierzcholkow for _ in range(ilosc_wierzcholkow)]

 

    for i in range(ilosc_wierzcholkow):

        for j in range(ilosc_wierzcholkow):

            if i != j:

                polaczenie = input(f"Czy istnieje połączenie między wierzchołkiem {i} a {j}? (tak/nie): ")

                if polaczenie == 'tak':

                    macierz_sasiedztwa[i][j] = 1

 

    print("\nMacierz sąsiedztwa:")

    for row in macierz_sasiedztwa:

        print(row)

 

    lista_sasiedztwa = [[] for _ in range(ilosc_wierzcholkow)]

    for i in range(ilosc_wierzcholkow):

        for j in range(ilosc_wierzcholkow):

            if macierz_sasiedztwa[i][j] == 1:

                lista_sasiedztwa[i].append(j)

 

    print("\nLista sąsiedztwa:")

    for i, sasiedzi in enumerate(lista_sasiedztwa):

        print(f"{i}: {sasiedzi}")

 

    interpretacja_graficzna = [[' ' for _ in range(ilosc_wierzcholkow)] for _ in range(ilosc_wierzcholkow)]

    for i in range(ilosc_wierzcholkow):

        for j in range(ilosc_wierzcholkow):

            if macierz_sasiedztwa[i][j] == 1:

                interpretacja_graficzna[i][j] = '1'

 

    print("\nInterpretacja graficzna:")

    for row in interpretacja_graficzna:

        print(' '.join(row))

 

 

graf()