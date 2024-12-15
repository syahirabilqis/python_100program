# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan : 15 Desember 2024
# Program Mengecek Angka Positif atau Negatif

print("*"*40)
print("Mengecek Angka Positif atau Negatif")
print("*"*40)

angka = float(input("Masukkan sebuah angka: "))

if angka > 0:
    print("angka Positif. ")
elif angka < 0:
    print("Angka negatif.")
else:
    print("Angka nol.")