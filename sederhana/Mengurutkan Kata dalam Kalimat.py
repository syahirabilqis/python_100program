# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan : 9 Januari 2025
# Program Mengurutkan Kata dalam Kalimat

print("*" * 40)
print("*Mengurutkan Kata dalam Kalimat")
print("*" * 40)

kalimat = input("Tulis Sebuah Kalimat: ")
kata = kalimat.split()
kata.sort()
print("Berikut Urutan Kata-Kata:")
for urut in kata:
   print(urut)