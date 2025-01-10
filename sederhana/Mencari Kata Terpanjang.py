# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan : 9 Januari 2025
# Program Program Mencari Kata Terpanjang

print("*" * 40)
print("Program Mencari Kata Terpanjang")
print("*" * 40)

kalimat = input("Masukkan sebuah kalimat: ")
kata_list = kalimat.split()

terpanjang = max(kata_list, key=len)

print(f"Kata terpanjang dalam kalimat ini adalah: '{terpanjang}' dengan panjang {len(terpanjang)} karakter.")