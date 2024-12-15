# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan : 12 Desember 2024
# Program Menentukan Tahun Kabisat

print("*" * 40)
print("Menentukan Tahun Kabisat")
print("*" * 40)

def cek_kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    else:
        return False

tahun = int(input("Masukkan tahun untuk cek kabisat: "))

if cek_kabisat(tahun):
    print(f"{tahun} adalah tahun kabisat.")
else:
    print(f"{tahun} bukan tahun kabisat.")