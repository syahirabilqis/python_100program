# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan :  13 Oktober 2024
# Program Limas Segitiga

print("*"*40)
print("Rumus Limas Segitiga")
print("*"*40)

a = float(input("Masukan Luas alas Segitiga: "))
s = float(input("Masukan Luas Sisi Tegak:  "))
t = float (input("Masukan Tinggi limas: "))

v = (1/3) * a * t
lp = a + s
la = 1/2 * a * t

print("Volume Limas Segitiga: ",v,"vol")
print("Luas Permukaan Limas Segitiga: ",lp,"m2")
print("Luas Alas Segitiga: ",la,"m2")
