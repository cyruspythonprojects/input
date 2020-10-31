# 3. Fråga användaren om när han/hon är född och beräkna hur gammal han/hon är. Ta endast hänsyn till året och ej månad/dag
print("Skriv in 0 för att avsluta.")
while True:
    try: 
        year = int(input("Vilket år är ni född: "))
        if year == 0:
            break
        print("Du är", 2020-year,"år")
    except:
        print("Något gick fel, försök igen...")