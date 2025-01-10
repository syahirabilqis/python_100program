# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan :  9 November 2024
# Program Menghitung Hari ke Tahun

print("*"*40)
print("Menghitung Hari ke Tahun")
print("*"*40)

HARI_PER_TAHUN = 365
HARI_PER_BULAN = 30
harii = int(input('Masukkan jumlah hari : '))

tahun = int(harii / HARI_PER_TAHUN)
harri = harii % HARI_PER_TAHUN

bulan = int(harri / HARI_PER_BULAN)
hari = harri % HARI_PER_BULAN

print(tahun, 'tahun', bulan, 'bulan', hari, 'hari')