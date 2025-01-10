# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan : 9 Januari 2025
# Program Cek Kata dalam Kalimat

print("*"*40)
print("Program Cek Kata dalam Kalimat")
print("*"*40)

kalimat = input("Masukkan sebuah kalimat: ")
kata = input("Masukkan kata yang ingin dicari: ")
if kata in kalimat:
    print("Kata ditemukan dalam kalimat.")
else:
    print("Kata tidak ditemukan.")