#Program przyjmuje dwie liczby zadane przez użytkownika i wykonuje na nich zlecone działanie

def kalkulator(dzialanie, liczba1, liczba2):
    if dzialanie == 1:
        wynik = liczba1 + liczba2
    elif dzialanie == 2:
        wynik = liczba1 - liczba2
    elif dzialanie == 3:
        wynik = liczba1 * liczba2
    elif dzialanie == 4:
        wynik = liczba1 / liczba2
    else:
        exit(1)
    return wynik

def sprawdz_dzialanie(dzialanie):
#Funkcja sprawdza, czy wprowadzono poprawną wartość zmiennej "dzialanie" i zwraca wartość boolean
    dopuszczalne_dzialania = ('0', '1', '2', '3', '4')
    if dzialanie in dopuszczalne_dzialania:
        return True
    else:
        return False
        

#Część wykonywalna
if __name__ == "__main__":

    #Ustalenie rodzaju działania matematycznego
    text_promptu = "Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie, 0 Zamknij: "  
    dzialanie = ""
    while sprawdz_dzialanie(dzialanie) == False:        #dopóki nie wpisano poprawnej liczby
        dzialanie = input(text_promptu)                 #wpisz numer działania
    
    if dzialanie == '0':                                #obsługa przypadku wyjścia
        print("Kończę pracę")
        exit(0)
    else:
        dzialanie = int(dzialanie)                      #jeżeli dzialanie poprawne, zmień na intergera i proceduj

    #Wpisanie składników działania
    


