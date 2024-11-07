# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan :  7 November 2024
# Program Kerucut Function

print("*"*40)
print("Program Kerucut Function")
print("*"*40)

def Kerucut():
    s = float(input("Masukan gasis lukis (s): "))
    r = float(input("Masukan jari2: "))
    t = float(input("Masukan tinggi: "))
    PHI = 3.14
    
    v = lambda r,PHI,t,s : 1/3 * PHI * r * r * t
    la = lambda r,PHI,t,s: PHI * r * r
    s = lambda r,t,s,PHI :(r**2 + t**2) ** 0.5
    selimut = lambda r,PHI,t,s : PHI * r * r
    lp = lambda r,t,s,PHI : PHI * r * r (r+s)
    kp = lambda r,t,s,PHI : 2 * PHI * r
    
    print("Luas Permukaan Kerucut: ",lp (r,t,s,PHI), "m2")
    print("Luas Alas Kerucut: ",la (s,r,t,PHI), "cm")
    print("Volume Kerucut: ",v (r,PHI,s,t), "cm")
    print("Keliling Kerucut: ",kp (r,t,s,PHI), "m")
    print("Selimut Kerucut: ",selimut (r,PHI,s,t), "cm")
    
Kerucut()