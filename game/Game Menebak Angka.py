# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan :  8 November 2024
# Game Menebak Angka

print("*"*40)
print("Game Menebak Angka")
print("*"*40)

import random

angka_rahasia = random.randint(1,100)

print("Selamat datang di permainan menebak angka!")
print("Saya telah memilih sebuah angka antara 1 sampai 100.")
print("Coba tebak angka tersebut!")

tebakan = None

while tebakan != angka_rahasia :
    tebakan = int(input("Masukkan tebakan Anda: "))
    
    if tebakan < angka_rahasia:
        print("Terlalu kecil!")
    elif tebakan > angka_rahasia:
        print("Terlalu Besar!")
    else:
        print("Selamat! Anda berhasil menebak angka tersebut.")
        