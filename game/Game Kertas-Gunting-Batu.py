# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan : 12 Desember 2024
# Program Game Kertas-Gunting-Batu

import random

print("*" * 40)
print("Selamat Datang di Game Batu-Gunting-Kertas!")
print("*" * 40)

def batu_gunting_kertas():
    pilihan = ["batu", "gunting", "kertas"]
    while True:
        print("\nPilihan: Batu, Gunting, Kertas")
        pemain = input("Masukkan pilihanmu: ").lower()
        if pemain not in pilihan:
            print("Pilihan tidak valid. Coba lagi!")
            continue

        komputer = random.choice(pilihan)
        print(f"Komputer memilih: {komputer}")

        if pemain == komputer:
            print("Hasil: Seri!")
        elif (pemain == "batu" and komputer == "gunting") or \
             (pemain == "gunting" and komputer == "kertas") or \
             (pemain == "kertas" and komputer == "batu"):
            print("Hasil: Kamu Menang!")
        else:
            print("Hasil: Kamu Kalah!")

        lagi = input("Main lagi? (ya/tidak): ").lower()
        if lagi != "ya":
            print("Terima kasih telah bermain!")
            break

batu_gunting_kertas()