# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan :  13 Oktober 2024
# Program Balok

print("*"*40)
print("Rumus Balok")
print("*"*40)

p = float(input("Masukan Panjang: "))
l = float(input("Masukan Lebar: "))
t = float(input("Masukan Tinggi: "))

lp = 2 * (p * l + p * t + l * t)
kp = 2 * (p + l)
v = p * l * t

print("Luas Balok: ",lp, "m2")
print("Keliling Balok: ",kp,"m")
print("Volume Balok: ",v, "vol")