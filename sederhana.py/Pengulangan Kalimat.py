# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan :  8 November 2024
# Program Pengulangan Kalimat

print("*"*40)
print("Program Pengulangan kalimat")
print("*"*40)

jumlah = int(input("Masukkan Jumlah Pengulangan: "))
kalimat = input("Masukkan Kalimat: ")

for i in range(jumlah):
    print(f"{i + 1}. {kalimat}")