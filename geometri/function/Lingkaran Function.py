# Dibuat oleh : Syahira Bilqis Humaira
# Tanggal pengerjaan :  8 November 2024
# Program Lingkaran Function

print("*"*40)
print("Program Lingkaran Function")
print("*"*40)

def Lingkaran():
    Jari2 = float(input("Masukan jari2 : "))
    lp = lambda Jari2 : 3.14 * Jari2 * Jari2
    kp = lambda Jari2 : 2*3.12 * Jari2
    print("Luas Lingkaran: ",lp (Jari2), "m")
    print("Keliling Lingkaran: ",kp (Jari2), "cm2")
    
Lingkaran()