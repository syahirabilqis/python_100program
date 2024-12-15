# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan :  22 November 2024
# Program Menghitung Huruf Vokal

print("*" * 40)
print("Menghitung Huruf Vokal")
print("*" * 40)

def hitung_vokal(teks):
    vokal = "aeiouAEIOU"
    jumlah = 0
    for huruf in teks:
        if huruf in vokal:
            jumlah += 1
    return jumlah

teks = input("Masukkan kalimat: ")
print("Jumlah huruf vokal: " , hitung_vokal(teks))