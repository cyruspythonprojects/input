# 2.Fråga användaren om namn och efternamn i två olika inputs. Skriv ut det hela namnet.
print("Tryck endast på ENTER för att avsluta.")
while True:
        fnamn = input("Skriv in förnamn: ")
        if fnamn == "":
            break
        enamn = input("Skriv in efternamn: ")
        if enamn == "":
            break
        print("Hela namnet är:",fnamn,enamn)