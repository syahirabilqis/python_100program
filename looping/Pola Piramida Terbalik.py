# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan : 16 Desember 2024
# Program Pola Piramida Terbalik

print("*"*40)
print("Pola Piramida Terbalik")
print("*"*40)

baris = int(input("Masukkan jumlah baris: "))
for i in range(baris, 0, -1):
    print(" " * (baris - i) + "* " * i)