# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan :  8 November 2024
# Program Cek Jodoh

print("*"*40)
print("Program Cek Jodoh")
print("*"*40)

import random

def cek_kecocokan(nama1, nama2):
    kecocokan = random.randint(50, 100)
    print(f"Tingkat kecocokan antara {nama1} dan {nama2} adalah {kecocokan}%.")

nama1 = input("Masukkan nama Anda: ")
nama2 = input("Masukkan nama pasangan Anda: ")
cek_kecocokan(nama1, nama2)