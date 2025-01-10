# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan : 9 Januari 2025
# Program Cek Bilangan Sempurna

print("*"*40)
print("Program Cek Bilangan Sempurna")
print("*"*40)

angka = int(input("Masukkan sebuah angka: "))
faktor_total = sum(i for i in range(1, angka) if angka % i == 0)

if faktor_total == angka:
    print(f"{angka} adalah bilangan sempurna.")
else:
    print(f"{angka} bukan bilangan sempurna.")