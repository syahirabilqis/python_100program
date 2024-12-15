# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan :  19 November 2024
# Program Mencari Tau Bilangan

print("*" * 40)
print("Mencari Tau Bilangan")
print("*" * 40)

angka = int(input("Masukkan nilai: "))

if angka > 100:
    print("angka adalah ratusan")
elif angka > 1000:
    print("angka adalah ribuan")
elif angka > 1000000:
    print("angka adalah jutaan")
else:
    print("coba lagi")