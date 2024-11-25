import random

choices = ["rock", "paper", "scissors"]

# machine_choice = random.choice(choices)


# bevezető
print("Üdvözölek a Kő, Papír, Olló játékban!")

# számlálók
nyerések = 0
vesztések = 0
döntetlenek = 0

# játék ciklus
while True:
    # játékos választása
    valasz = input("Válasz karaktert: Kő, Papír, Olló -> ").strip().lower()

    # ellenőrzés
    if valasz not in ["kő", "papír", "olló"]:
        print("Érvénytelen válasz, próbáld újra!")
        continue

    # gép választása
    gep_valasz = random.choice(["kő", "papír", "olló"])
    print(f"Gép választása: {gep_valasz}")

    # győztes
    if valasz == gep_valasz:
        print("Döntetlen!")
        döntetlenek += 1
    elif (valasz == "kő" and gep_valasz == "olló") or (valasz == "papír" and gep_valasz == "kő") or (valasz == "olló" and gep_valasz == "papír"):
        print("Nyertél!")
        nyerések += 1
    else:
        print("Vesztettél!")
        vesztések += 1

    # eredmények
    print(f"nyerések: {nyerések}, vesztések: {vesztések}, döntetlenek: {döntetlenek}")

    # új játék
    uj_jatek = input("Akarsz még játszani? (i/n) ").strip().lower()
    if uj_jatek != "i":
        break

# összegzés
print(f"Köszönjük a játékot! A végső eredmény: {nyerések} győzelem, {vesztések} vereség, {döntetlenek} döntetlen. Várunk vissza legközelebb! :)")
