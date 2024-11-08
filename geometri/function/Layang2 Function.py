# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan :  8 November 2024
# Program Layang-Layang Function

print("*"*40)
print("Program Layang-Layang Function")
print("*"*40)

def Layang2():
    diagonal1 = float(input("Masukkan d1 : "))
    diagonal2 = float(input("Masukkan d2 : "))
    s1 = float(input("Masukkan sisi 1 : "))
    s2 = float(input("Masukan sisi 2 : "))
    
    l = diagonal1 * diagonal2 / 2
    k = 2 * s1 * s2
    
    print("Luas Layang-Layang: ",l,"m2")
    print("Keliling Layang-Layang: ",k, "cm2")
    
Layang2()