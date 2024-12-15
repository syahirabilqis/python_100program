# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan :  25 Oktober 2024
# Program Game Tebak Angka

print("*" * 40)
print("Selamat Datang di Game Tebak Angka!")
print("*" * 40)

import random

def tebak_angka():
    angka_rahasia = random.randint(1, 100) 
    percobaan = 0
    print("Saya sudah memilih angka antara 1 hingga 100. Coba tebak!")

    while True:
        tebak = input("Masukkan tebakanmu: ")
        if not tebak.isdigit():  
            print("Mohon masukkan angka yang valid.")
            continue

        tebak = int(tebak)  
        percobaan += 1  

        if tebak < angka_rahasia:
            print("Tebakanmu terlalu kecil.")
        elif tebak > angka_rahasia:
            print("Tebakanmu terlalu besar.")
        else:
            print(f"Selamat! Tebakanmu benar. Angka rahasia adalah {angka_rahasia}.")
            print(f"Kamu berhasil menebaknya dalam {percobaan} percobaan.")
            break

tebak_angka()