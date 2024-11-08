# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan :  8 November 2024
# Program Persegi  Function

print("*"*40)
print("Program Persegi Function")
print("*"*40)

def Persegi():
    s = float(input("Masukan Sisi : "))
    lp = lambda s : s * s
    kp = lambda s: s * s * s * s
    
    print("Luas Persegi: ",lp (s), "m2")
    print("keliling Persegi: ",kp (s), "m")
    
Persegi()