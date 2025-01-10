# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan : 15 Desember 2024
# Program Menghilangkan tanda baca

print("*"*40)
print("Menghilangkan Tanda Baca")
print("*"*40)

teks_asli = input("Masukkan kata: ")

def hapus_tanda_baca(teks):
    tanda_baca = ".,!?;:-_\"'()[]{}<>@#%^&*~`/|\\"
    teks_bersih = ""
    for karakter in teks:
        if karakter not in tanda_baca:
            teks_bersih += karakter
    return teks_bersih

teks_bersih = hapus_tanda_baca(teks_asli)

print("Teks Asli:", teks_asli)
print("Teks Bersih:", teks_bersih)