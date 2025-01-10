# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan : 9 Januari 2025
# Program Mata uang USD

print("*"*40)
print("Program Mata uang USD")
print("*"*40)

usd = float(input("Masukkan jumlah dalam USD: "))
kurs = 15000 
idr = usd * kurs
print(f"${usd:.2f} sama dengan Rp{idr:.2f}")