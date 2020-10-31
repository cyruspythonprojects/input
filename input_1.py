# 1.Fråga användaren om två olika tal, addera dessa tal och skriv ut dem på skärmen.
print("Skriv in 0 för att avsluta.")
while True:
    try:
        tal_1 = float(input("Skriv in första talet: "))
        if tal_1 == 0:
            break
        tal_2 = float(input("Skriv in andra talet: "))
        if tal_2 == 0:
            break
        print("Summan blir:",tal_1+tal_2)
    except ValueError:
        print("Fel input: var god skriv in enbart siffror, försök igen.")