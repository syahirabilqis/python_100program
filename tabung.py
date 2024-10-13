# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan :  13 Oktober 2024
# Program Tabung

print("*"*40)
print("Rumus Tabung")
print("*"*40)

r = float(input("Masukan Jari2: "))
t = float(input("Masukan Tinggi: "))

PHI = 3.14

lp = 2 * PHI * r * (r * t)
kp = 2 * PHI * r

print("Luas Tabung: ",lp,"m2")
print("Keliling Tabung: ",kp,"m")