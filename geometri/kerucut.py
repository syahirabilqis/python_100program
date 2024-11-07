# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan :  11 Oktober 2024
# Program Kerucut

print("*"*40)
print("Rumus Kerucut")
print("*"*40)

r = float(input("Masukan jari2: "))
t = float(input("Masukan tinggi: "))

PHI = 3.14
s = (r**2 + t**2) ** 0.5

lp = PHI * r * r (r + s)
kp = 2 * PHI * r

print("Luas Kerucut: ", lp, "m2")
print("Keliling Kerucut: ",kp, "m")
