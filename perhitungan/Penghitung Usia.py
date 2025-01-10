# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan : 12 Desember 2024
# Program Penghitung Usia

print("*" * 40)
print("Penghitung Usia")
print("*" * 40)

from datetime import date

tahun_lahir = int(input("Masukkan tahun lahir Anda: "))

tahun_sekarang = date.today().year
usia = tahun_sekarang - tahun_lahir

print(f"Usia Anda: {usia} tahun")