# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan : 12 Desember 2024
# Program Game Tebak Warna

import random

print("*" * 40)
print("Selamat Datang di Game Tebak Warna!")
print("*" * 40)

def tebak_warna():
    warna = ["merah", "biru", "kuning", "hijau", "ungu", "putih", "hitam"]
    warna_rahasia = random.choice(warna)
    print("Saya telah memilih salah satu warna ini:")
    print(", ".join(warna))

    while True:
        tebakan = input("Tebak warna saya: ").lower()

        if tebakan == warna_rahasia:
            print("Selamat! Tebakanmu benar!")
            break
        else:
            print("Salah! Coba lagi.")
tebak_warna()