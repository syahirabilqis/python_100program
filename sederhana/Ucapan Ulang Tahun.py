# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan : 7 januari 2025
# Program ucapan ulang tahun

print("*"*40)
print("Program ucapan ulang tahun")
print("*"*40)

nama = input("Masukkan nama kamu: ")
print("DD >> day / hari MM >> month / bulan")
tanggal = input("Masukkan tanggal ulang tahunmu (format: DD-MM): ")


from datetime import datetime
hari_ini = datetime.now().strftime("%d-%m")

if tanggal == hari_ini:
    print(f"Selamat ulang tahun, {nama}! Semoga hari-harimu menyenangkan!")
else:
    print(f"Hari ini bukan ulang tahunmu, {nama}. Tetap semangat ya!")