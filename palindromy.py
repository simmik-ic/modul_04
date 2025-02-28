def czypalindrom(dany_tekst):
    """
        Sprawdza, czy dany string jest palindromem, 
        tzn. czy czytany od przodu i od tyłu brzmi tak samo.
        Argument: string
    """
    tekst_bez_spacji = str(dany_tekst).replace(" ", "").lower()
    i = 1

    for i in range(0, len(tekst_bez_spacji)//2):
        if tekst_bez_spacji[i] != tekst_bez_spacji[-(i+1)]:
            return False
    
    return True
   

#debug line do usunięcia przed wysłaniem
print(czypalindrom("Mamuta tu mam"))