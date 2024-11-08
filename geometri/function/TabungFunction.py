# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan :  8 November 2024
# Program Tabung Function

print("*"*40)
print("Program Tabung Function")
print("*"*40)

def Tabung():
    r = float(input("Masukan Jari2: "))
    t = float(input("Masukan Tinggi: "))
    PHI = 3.14
    
    lp = lambda r,t : 2 * PHI * r * (r * t)
    kp = lambda r,t : 2 * PHI * r
    
    print("Luas Tabung: ",lp (r,t),"m2")
    print("Keliling Tabung: ",kp (r,t),"m")
    
Tabung()