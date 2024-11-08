# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan :  8 November 2024
# Program Trapesium Function

print("*"*40)
print("Program Trapesium Function")
print("*"*40)

def Trapesium():
    a = float(input("Masukan sisi a: "))
    b = float(input("Masukan sisi b: "))
    c = float(input('Masukan sisi c: '))
    d = float(input("Masukan sisi d: "))
    t = float(input("Masukan tinggi: "))
    
    lp = lambda a,b,c,d,t : 1/2 * (a + b) * t
    kp = lambda a,b,c,d,t : a + b + c + d
    
    print("Luas Trapesium: ",lp (a,b,c,d,t), "cm2")
    print("Keliling Trapesium: ",kp (a,b,c,d,t), "m")
    
Trapesium()