print("*" *40)
print("Program Game Tebak Kepala atau Ekor")
print("*"*40)

import random

print("Selamat datang di game Tebak Kepala atau Ekor!")
print("Ketik 'kepala' atau 'ekor' untuk bermain.\n")

pilihan = ["kepala", "ekor"]

while True:
    komputer = random.choice(pilihan)
    tebakan = input("Tebakanmu (kepala/ekor): ").lower()

    if tebakan not in pilihan:
        print("Input tidak valid. Coba lagi!")
        continue

    if tebakan == komputer:
        print(f"Benar! Komputer memilih {komputer}.")
    else:
        print(f"Salah! Komputer memilih {komputer}.")
    
    lagi = input("Main lagi? (ya/tidak): ").lower()
    if lagi != "ya":
        print("Terima kasih sudah bermain!")
        break