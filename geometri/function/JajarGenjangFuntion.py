# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan :  7 November 2024
# Program JajarGenjang Function

print("*"*40)
print("Program Jarjar Genjang Lambda")
print("*"*40)

def JajarGenjang():
    a = float(input("Masukan alas: "))
    t = float(input("Masukan tinggi: "))
    p = float(input("Masukan panjang: "))
    l = float(input("Masukan lebar: "))
    lp = lambda a,t,p,l : a * t
    kp = lambda a,t,p,l : 2 * p * l
    
    print("Luas Jajar Genjang: ",lp (a,t,p,l), "m2")
    print("Keliling Jajar Genjang: ",kp (a,t,p,l), "m")
    
JajarGenjang()