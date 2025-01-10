# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan : 9 Januari 2025
# Program Game Dadu

print("*" *40)
print("Program Game Dadu")
print("*"*40)
import random

def game_dadu():
    while True:
        input("Tekan Enter untuk menggulung dadu...")
        hasil = random.randint(1, 6)
        print(f"Anda mendapatkan angka: {hasil}")

        lagi = input("Ingin menggulung lagi? (y/n): ").lower()
        if lagi != 'y':
            print("Terima kasih telah bermain!")
            break

game_dadu()