# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan :  8 November 2024
# Program Ramalan keberuntungan

print("*"*40)
print("Program Ramalan Keberuntungan")
print("*"*40)

import random

def ramalan_keberuntungan(tanggal):
    print("Meramal keberuntungan Anda berdasarkan tanggal lahir...")
    nasib = [
        "Hari ini adalah hari keberuntungan Anda!",
        "Waspadalah, ada energi negatif yang mengintai.",
        "Keberuntungan akan datang dari arah yang tidak terduga.",
        "Hindari keputusan besar hari ini.",
        "Kesehatan Anda akan meningkat, terus jaga pola makan."
    ]
    print(f"Ramalan untuk {tanggal}: {random.choice(nasib)}")

tanggal_lahir = input("Masukkan tanggal lahir Anda (hari-bulan-tahun): ")
ramalan_keberuntungan(tanggal_lahir)