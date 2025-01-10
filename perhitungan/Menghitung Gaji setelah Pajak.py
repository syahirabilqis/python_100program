# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan : 9 Januari 2025
# Program Menghitung Gaji setelah Pajak

print("*"*40)
print("Program Menghitung Gaji setelah Pajak")
print("*"*40)

gaji = float(input("Masukkan gaji bulanan: "))
pajak = float(input("Masukkan persentase pajak: "))
gaji_bersih = gaji - (gaji * pajak / 100)
print(f"Gaji setelah pajak: {gaji_bersih}")