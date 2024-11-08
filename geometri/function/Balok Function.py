# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan :  7 November 2024
# Program Balok Function

print("*"*40)
print("Program Balok Lambda")
print("*"*40)

def balok():
    p = float(input("Masukan Panjang: "))
    l = float(input("Masukan Lebar: "))
    t = float(input("Masukan Tinggi: "))
    v = lambda p,l,t : p * l * t
    lp = lambda p,l,t : 2 * (p * l + p * t + l * t)
    kp = lambda p,l,t : 2 * (p + l)
    
    print("Luas Balok: ",lp (p,l,t), "m2")
    print("Keliling Balok: ",kp(p,l,t),"m")
    print("Volume Balok: ",v(p,l,t), "vol")
    
balok()