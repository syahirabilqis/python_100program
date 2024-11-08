# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan :  7 November 2024
# Program Kerucut Function

print("*" * 40)
print("Program Kerucut Function")
print("*" * 40)

def Kerucut():
    s = float(input("Masukkan garis lukis (s): "))
    r = float(input("Masukkan jari-jari (r): "))
    t = float(input("Masukkan tinggi (t): "))
    PHI = 3.14

    v = lambda r, PHI, t: 1/3 * PHI * r * r * t
    la = lambda r, PHI: PHI * r * r
    s_calc = lambda r, t: (r*2 + t*2) ** 0.5  # Menghitung panjang garis lukis jika tidak diketahui
    selimut = lambda r, PHI, s: PHI * r * s
    lp = lambda r, s, PHI: PHI * r * (r + s)
    kp = lambda r, PHI: 2 * PHI * r

    print("Luas Permukaan Kerucut: ", lp(r, s, PHI), "m2")
    print("Luas Alas Kerucut: ", la(r, PHI), "cm2")
    print("Volume Kerucut: ", v(r, PHI, t), "cm3")
    print("Keliling Alas Kerucut: ", kp(r, PHI), "m")
    print("Selimut Kerucut: ", selimut(r, PHI, s), "cm")

Kerucut()