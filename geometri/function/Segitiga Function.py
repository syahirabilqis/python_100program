# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan :  8 November 2024
# Program Segitiga Function

print("*"*40)
print("Program Segitiga Function")
print("*"*40)

def Segitiga():
    t = float(input("Masukan Tinggi: "))
    a = float(input("Masukan Alas: "))
    s = float(input("Masukan Sisi: "))
    
    lp = lambda t,a,s : 1/2 * a * t
    kp = lambda t,a,s : s * s * s
    
    print("Luas Segitiga: ",lp (t,a,s), "m2")
    print("Keliling Segitiga: ",kp (t,a,s), "m")
    
Segitiga()