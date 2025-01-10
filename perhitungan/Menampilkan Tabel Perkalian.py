# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan : 9 Januari 2025
# Program Tabel Perkalian

print("*" * 40)
print("Program Tabel Perkalian")
print("*" * 40)

angka = int(input("Masukkan angka untuk tabel perkalian: "))

for i in range(1, 11):
    print(f"{angka} x {i} = {angka * i}")