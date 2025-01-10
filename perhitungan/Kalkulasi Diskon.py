# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan :  8 November 2024
# Program Kalkulasi Diskon

print("*"*40)
print("Program Kalkulasi Diskon")
print("*"*40)

harga = float(input("Masukkan Harga Produk: "))
diskon = float(input("Masukkan Persentase Diskon: "))
harga_akhir = harga - (harga * diskon / 100)
print(f"Harga Setelah Diskon adalah: {harga_akhir}")